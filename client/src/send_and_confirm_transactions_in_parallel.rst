client/src/send_and_confirm_transactions_in_parallel.rs
=======================================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use {
    crate::{
        nonblocking::{rpc_client::RpcClient, tpu_client::TpuClient},
        rpc_client::RpcClient as BlockingRpcClient,
    },
    bincode::serialize,
    dashmap::DashMap,
    solana_quic_client::{QuicConfig, QuicConnectionManager, QuicPool},
    solana_rpc_client::spinner,
    solana_rpc_client_api::{
        client_error::ErrorKind,
        request::{RpcError, RpcResponseErrorData, MAX_GET_SIGNATURE_STATUSES_QUERY_ITEMS},
    },
    solana_sdk::{
        hash::Hash,
        message::Message,
        signature::{Signature, SignerError},
        signers::Signers,
        transaction::{Transaction, TransactionError},
    },
    solana_tpu_client::{
        nonblocking::tpu_client::set_message_for_confirmed_transactions,
        tpu_client::{Result, TpuSenderError},
    },
    std::{
        sync::{
            atomic::{AtomicU32, AtomicU64, Ordering},
            Arc,
        },
        time::Duration,
    },
    tokio::{sync::RwLock, task::JoinHandle, time::Instant},
};

const BLOCKHASH_REFRESH_RATE: Duration = Duration::from_secs(10);
const TPU_RESEND_REFRESH_RATE: Duration = Duration::from_secs(2);
type QuicTpuClient = TpuClient<QuicPool, QuicConnectionManager, QuicConfig>;

#[derive(Clone, Debug)]
struct TransactionData {
    last_valid_blockheight: u64,
    message: Message,
    index: usize,
    serialized_transaction: Vec<u8>,
}

#[derive(Clone, Debug, Copy)]
struct BlockHashData {
    pub blockhash: Hash,
    pub last_valid_blockheight: u64,
}

#[derive(Clone, Debug, Copy)]
pub struct SendAndConfrimConfig {
    pub with_spinner: bool,
    pub resign_txs_count: Option<usize>,
}

pub fn send_and_confirm_transactions_in_parallel_blocking<T: Signers + ?Sized>(
    rpc_client: Arc<BlockingRpcClient>,
    tpu_client: Option<QuicTpuClient>,
    messages: &[Message],
    signers: &T,
    config: SendAndConfrimConfig,
) -> Result<Vec<Option<TransactionError>>> {
    let fut = send_and_confirm_transactions_in_parallel(
        rpc_client.get_inner_client().clone(),
        tpu_client,
        messages,
        signers,
        config,
    );
    tokio::task::block_in_place(|| rpc_client.runtime().block_on(fut))
}

fn create_blockhash_data_updating_task(
    rpc_client: Arc<RpcClient>,
    blockhash_data_rw: Arc<RwLock<BlockHashData>>,
    current_block_height: Arc<AtomicU64>,
) -> JoinHandle<()> {
    tokio::spawn(async move {
        loop {
            if let Ok((blockhash, last_valid_blockheight)) = rpc_client
                .get_latest_blockhash_with_commitment(rpc_client.commitment())
                .await
            {
                *blockhash_data_rw.write().await = BlockHashData {
                    blockhash,
                    last_valid_blockheight,
                };
            }

            if let Ok(blockheight) = rpc_client.get_block_height().await {
                current_block_height.store(blockheight, Ordering::Relaxed);
            }
            tokio::time::sleep(BLOCKHASH_REFRESH_RATE).await;
        }
    })
}

fn create_transaction_confirmation_task(
    rpc_client: Arc<RpcClient>,
    current_block_height: Arc<AtomicU64>,
    unconfirmed_transasction_map: Arc<DashMap<Signature, TransactionData>>,
    errors_map: Arc<DashMap<usize, TransactionError>>,
    num_confirmed_transactions: Arc<AtomicU32>,
) -> JoinHandle<()> {
    tokio::spawn(async move {
        // check transactions that are not expired or have just expired between two checks
        let mut last_block_height = current_block_height.load(Ordering::Relaxed);

        loop {
            if !unconfirmed_transasction_map.is_empty() {
                let current_block_height = current_block_height.load(Ordering::Relaxed);
                let transactions_to_verify: Vec<Signature> = unconfirmed_transasction_map
                    .iter()
                    .filter(|x| {
                        let is_not_expired = current_block_height <= x.last_valid_blockheight;
                        // transaction expired between last and current check
                        let is_recently_expired = last_block_height <= x.last_valid_blockheight
                            && current_block_height > x.last_valid_blockheight;
                        is_not_expired || is_recently_expired
                    })
                    .map(|x| *x.key())
                    .collect();
                for signatures in
                    transactions_to_verify.chunks(MAX_GET_SIGNATURE_STATUSES_QUERY_ITEMS)
                {
                    if let Ok(result) = rpc_client.get_signature_statuses(signatures).await {
                        let statuses = result.value;
                        for (signature, status) in signatures.iter().zip(statuses.into_iter()) {
                            if let Some((status, data)) = status
                                .filter(|status| {
                                    status.satisfies_commitment(rpc_client.commitment())
                                })
                                .and_then(|status| {
                                    unconfirmed_transasction_map
                                        .remove(signature)
                                        .map(|(_, data)| (status, data))
                                })
                            {
                                num_confirmed_transactions.fetch_add(1, Ordering::Relaxed);
                                if let Some(error) = status.err {
                                    errors_map.insert(data.index, error);
                                }
                            };
                        }
                    }
                }

                last_block_height = current_block_height;
            }
            tokio::time::sleep(Duration::from_secs(1)).await;
        }
    })
}

#[derive(Clone, Debug)]
struct SendingContext {
    unconfirmed_transasction_map: Arc<DashMap<Signature, TransactionData>>,
    error_map: Arc<DashMap<usize, TransactionError>>,
    blockhash_data_rw: Arc<RwLock<BlockHashData>>,
    num_confirmed_transactions: Arc<AtomicU32>,
    total_transactions: usize,
    current_block_height: Arc<AtomicU64>,
}

async fn sign_all_messages_and_send<T: Signers + ?Sized>(
    progress_bar: &Option<indicatif::ProgressBar>,
    rpc_client: Arc<RpcClient>,
    tpu_client: &Option<QuicTpuClient>,
    messages_with_index: Vec<(usize, Message)>,
    signers: &T,
    context: &SendingContext,
) -> Result<()> {
    let current_transaction_count = messages_with_index.len();
    // send all the transaction messages
    for (counter, (index, message)) in messages_with_index.iter().enumerate() {
        let mut transaction = Transaction::new_unsigned(message.clone());
        let blockhashdata = *context.blockhash_data_rw.read().await;

        // we have already checked if all transactions are signable.
        transaction
            .try_sign(signers, blockhashdata.blockhash)
            .expect("Transaction should be signable");
        let serialized_transaction = serialize(&transaction).expect("Transaction should serailize");
        let send_over_rpc = if let Some(tpu_client) = tpu_client {
            !tpu_client
                .send_wire_transaction(serialized_transaction.clone())
                .await
        } else {
            true
        };
        if send_over_rpc {
            if let Err(e) = rpc_client.send_transaction(&transaction).await {
                match &e.kind {
                    ErrorKind::Io(_) | ErrorKind::Reqwest(_) => {
                        // fall through on io error, we will retry the transaction
                    }
                    ErrorKind::TransactionError(transaction_error) => {
                        context.error_map.insert(*index, transaction_error.clone());
                        continue;
                    }
                    ErrorKind::RpcError(rpc_error) => {
                        if let RpcError::RpcResponseError {
                            data:
                                RpcResponseErrorData::SendTransactionPreflightFailure(simulation_result),
                            ..
                        } = rpc_error
                        {
                            if let Some(transaction_error) = &simulation_result.err {
                                context.error_map.insert(*index, transaction_error.clone());
                                continue;
                            }
                        }
                        return Err(TpuSenderError::from(e));
                    }
                    _ => {
                        return Err(TpuSenderError::from(e));
                    }
                }
            }
        }

        let signature = transaction.signatures[0];
        // send to confirm the transaction
        context.unconfirmed_transasction_map.insert(
            signature,
            TransactionData {
                index: *index,
                serialized_transaction,
                last_valid_blockheight: blockhashdata.last_valid_blockheight,
                message: message.clone(),
            },
        );

        if let Some(progress_bar) = progress_bar {
            set_message_for_confirmed_transactions(
                progress_bar,
                context
                    .num_confirmed_transactions
                    .load(std::sync::atomic::Ordering::Relaxed),
                context.total_transactions,
                None,
                blockhashdata.last_valid_blockheight,
                &format!(
                    "Sending {}/{} transactions",
                    counter + 1,
                    current_transaction_count,
                ),
            );
        }
    }
    Ok(())
}

async fn confirm_transactions_till_block_height_and_resend_unexpired_transaction_over_tpu(
    progress_bar: &Option<indicatif::ProgressBar>,
    tpu_client: &Option<QuicTpuClient>,
    context: &SendingContext,
) {
    let unconfirmed_transasction_map = context.unconfirmed_transasction_map.clone();
    let num_confirmed_transactions = context.num_confirmed_transactions.clone();
    let current_block_height = context.current_block_height.clone();
    let total_transactions = context.total_transactions;

    let transactions_to_confirm = unconfirmed_transasction_map.len();
    let max_valid_block_height = unconfirmed_transasction_map
        .iter()
        .map(|x| x.last_valid_blockheight)
        .max();

    if let Some(mut max_valid_block_height) = max_valid_block_height {
        if let Some(progress_bar) = progress_bar {
            set_message_for_confirmed_transactions(
                progress_bar,
                num_confirmed_transactions.load(std::sync::atomic::Ordering::Relaxed),
                total_transactions,
                Some(current_block_height.load(Ordering::Relaxed)),
                max_valid_block_height,
                &format!(
                    "Waiting for next block, {transactions_to_confirm} transactions pending..."
                ),
            );
        }

        // wait till all transactions are confirmed or we have surpassed max processing age for the last sent transaction
        while !unconfirmed_transasction_map.is_empty()
            && current_block_height.load(Ordering::Relaxed) < max_valid_block_height
        {
            let blockheight = current_block_height.load(Ordering::Relaxed);

            if let Some(progress_bar) = progress_bar {
                set_message_for_confirmed_transactions(
                    progress_bar,
                    num_confirmed_transactions.load(std::sync::atomic::Ordering::Relaxed),
                    total_transactions,
                    Some(blockheight),
                    max_valid_block_height,
                    "Checking transaction status...",
                );
            }

            if let Some(tpu_client) = tpu_client {
                let instant = Instant::now();
                // retry sending transaction only over TPU port
                // any transactions sent over RPC will be automatically rebroadcast by the RPC server
                let txs_to_resend_over_tpu = unconfirmed_transasction_map
                    .iter()
                    .filter(|x| blockheight < x.last_valid_blockheight)
                    .map(|x| x.serialized_transaction.clone())
                    .collect();
                let _ = tpu_client
                    .try_send_wire_transaction_batch(txs_to_resend_over_tpu)
                    .await;

                let elapsed = instant.elapsed();
                if elapsed < TPU_RESEND_REFRESH_RATE {
                    tokio::time::sleep(TPU_RESEND_REFRESH_RATE - elapsed).await;
                }
            } else {
                tokio::time::sleep(Duration::from_millis(100)).await;
            }
            if let Some(max_valid_block_height_in_remaining_transaction) =
                unconfirmed_transasction_map
                    .iter()
                    .map(|x| x.last_valid_blockheight)
                    .max()
            {
                max_valid_block_height = max_valid_block_height_in_remaining_transaction;
            }
        }

        if let Some(progress_bar) = progress_bar {
            set_message_for_confirmed_transactions(
                progress_bar,
                num_confirmed_transactions.load(std::sync::atomic::Ordering::Relaxed),
                total_transactions,
                Some(current_block_height.load(Ordering::Relaxed)),
                max_valid_block_height,
                "Checking transaction status...",
            );
        }
    }
}

/// This is a new method which will be able to send and confirm a large amount of transactions
/// The sending and confirmation of transactions is done in parallel tasks
/// The signer sign the transaction just before sending so that blockhash is not expired
pub async fn send_and_confirm_transactions_in_parallel<T: Signers + ?Sized>(
    rpc_client: Arc<RpcClient>,
    tpu_client: Option<QuicTpuClient>,
    messages: &[Message],
    signers: &T,
    config: SendAndConfrimConfig,
) -> Result<Vec<Option<TransactionError>>> {
    // get current blockhash and corresponding last valid block height
    let (blockhash, last_valid_blockheight) = rpc_client
        .get_latest_blockhash_with_commitment(rpc_client.commitment())
        .await?;
    let blockhash_data_rw = Arc::new(RwLock::new(BlockHashData {
        blockhash,
        last_valid_blockheight,
    }));

    // check if all the messages are signable by the signers
    messages
        .iter()
        .map(|x| {
            let mut transaction = Transaction::new_unsigned(x.clone());
            transaction.try_sign(signers, blockhash)
        })
        .collect::<std::result::Result<Vec<()>, SignerError>>()?;

    // get current blockheight
    let block_height = rpc_client.get_block_height().await?;
    let current_block_height = Arc::new(AtomicU64::new(block_height));

    let progress_bar = config.with_spinner.then(|| {
        let progress_bar = spinner::new_progress_bar();
        progress_bar.set_message("Setting up...");
        progress_bar
    });

    // blockhash and blockheight update task
    let block_data_task = create_blockhash_data_updating_task(
        rpc_client.clone(),
        blockhash_data_rw.clone(),
        current_block_height.clone(),
    );

    let unconfirmed_transasction_map = Arc::new(DashMap::<Signature, TransactionData>::new());
    let error_map = Arc::new(DashMap::new());
    let num_confirmed_transactions = Arc::new(AtomicU32::new(0));
    // tasks which confirms the transactions that were sent
    let transaction_confirming_task = create_transaction_confirmation_task(
        rpc_client.clone(),
        current_block_height.clone(),
        unconfirmed_transasction_map.clone(),
        error_map.clone(),
        num_confirmed_transactions.clone(),
    );

    // transaction sender task
    let total_transactions = messages.len();
    let mut initial = true;
    let signing_count = config.resign_txs_count.unwrap_or(1);
    let context = SendingContext {
        unconfirmed_transasction_map: unconfirmed_transasction_map.clone(),
        blockhash_data_rw: blockhash_data_rw.clone(),
        num_confirmed_transactions: num_confirmed_transactions.clone(),
        current_block_height: current_block_height.clone(),
        error_map: error_map.clone(),
        total_transactions,
    };

    for expired_blockhash_retries in (0..signing_count).rev() {
        // only send messages which have not been confirmed
        let messages_with_index: Vec<(usize, Message)> = if initial {
            initial = false;
            messages.iter().cloned().enumerate().collect()
        } else {
            // remove all the confirmed transactions
            unconfirmed_transasction_map
                .iter()
                .map(|x| (x.index, x.message.clone()))
                .collect()
        };

        if messages_with_index.is_empty() {
            break;
        }

        // clear the map so that we can start resending
        unconfirmed_transasction_map.clear();

        sign_all_messages_and_send(
            &progress_bar,
            rpc_client.clone(),
            &tpu_client,
            messages_with_index,
            signers,
            &context,
        )
        .await?;

        // wait until all the transactions are confirmed or expired
        confirm_transactions_till_block_height_and_resend_unexpired_transaction_over_tpu(
            &progress_bar,
            &tpu_client,
            &context,
        )
        .await;

        if unconfirmed_transasction_map.is_empty() {
            break;
        }

        if let Some(progress_bar) = &progress_bar {
            progress_bar.println(format!(
                "Blockhash expired. {expired_blockhash_retries} retries remaining"
            ));
        }
    }

    block_data_task.abort();
    transaction_confirming_task.abort();
    if unconfirmed_transasction_map.is_empty() {
        let mut transaction_errors = vec![None; messages.len()];
        for iterator in error_map.iter() {
            transaction_errors[*iterator.key()] = Some(iterator.value().clone());
        }
        Ok(transaction_errors)
    } else {
        Err(TpuSenderError::Custom("Max retries exceeded".into()))
    }
}


