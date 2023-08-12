state_synchronizer/src/executor_proxy.rs
========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::LedgerInfo;
use failure::prelude::*;
use futures::{channel::oneshot, Future, FutureExt};
use grpcio::EnvBuilder;
use solana_libra_config::config::NodeConfig;
use solana_libra_executor::Executor;
use solana_libra_logger::prelude::*;
use solana_libra_network::proto::GetChunkResponse;
use solana_libra_storage_client::{StorageRead, StorageReadServiceClient};
use solana_libra_types::{
    crypto_proxies::{LedgerInfoWithSignatures, ValidatorVerifier},
    transaction::TransactionListWithProof,
};
use solana_libra_vm_runtime::MoveVM;
use std::{pin::Pin, sync::Arc};

/// Proxies interactions with execution and storage for state synchronization
pub trait ExecutorProxyTrait: Sync + Send {
    /// Return the latest known version
    fn get_latest_version(&self) -> Pin<Box<dyn Future<Output = Result<u64>> + Send>>;

    /// Return the latest known ledger info
    fn get_latest_ledger_info(&self) -> Pin<Box<dyn Future<Output = Result<LedgerInfo>> + Send>>;

    /// Execute and commit a batch of transactions
    fn execute_chunk(
        &self,
        txn_list_with_proof: TransactionListWithProof,
        ledger_info_with_sigs: LedgerInfoWithSignatures,
    ) -> Pin<Box<dyn Future<Output = Result<()>> + Send>>;

    /// Gets chunk of transactions
    fn get_chunk(
        &self,
        known_version: u64,
        limit: u64,
        target: LedgerInfoWithSignatures,
    ) -> Pin<Box<dyn Future<Output = Result<GetChunkResponse>> + Send>>;

    fn validate_ledger_info(&self, target: &LedgerInfoWithSignatures) -> Result<()>;
}

pub(crate) struct ExecutorProxy {
    storage_read_client: Arc<StorageReadServiceClient>,
    executor: Arc<Executor<MoveVM>>,
    validator_verifier: ValidatorVerifier,
}

impl ExecutorProxy {
    pub(crate) fn new(executor: Arc<Executor<MoveVM>>, config: &NodeConfig) -> Self {
        let client_env = Arc::new(EnvBuilder::new().name_prefix("grpc-coord-").build());
        let storage_read_client = Arc::new(StorageReadServiceClient::new(
            client_env,
            &config.storage.address,
            config.storage.port,
        ));
        let validator_verifier = config.consensus.consensus_peers.get_validator_verifier();
        Self {
            storage_read_client,
            executor,
            validator_verifier,
        }
    }
}

fn convert_to_future<T: Send + 'static>(
    receiver: oneshot::Receiver<Result<T>>,
) -> Pin<Box<dyn Future<Output = Result<T>> + Send>> {
    async move {
        match receiver.await {
            Ok(Ok(t)) => Ok(t),
            Ok(Err(err)) => Err(format_err!("Failed to process request: {}", err)),
            Err(oneshot::Canceled) => {
                Err(format_err!("Executor Internal error: sender is dropped."))
            }
        }
    }
        .boxed()
}

impl ExecutorProxyTrait for ExecutorProxy {
    fn get_latest_version(&self) -> Pin<Box<dyn Future<Output = Result<u64>> + Send>> {
        let client = Arc::clone(&self.storage_read_client);
        async move {
            let resp = client.get_startup_info_async().await?;
            resp.map(|r| r.latest_version)
                .ok_or_else(|| format_err!("failed to fetch startup info"))
        }
            .boxed()
    }

    fn get_latest_ledger_info(&self) -> Pin<Box<dyn Future<Output = Result<LedgerInfo>> + Send>> {
        let client = Arc::clone(&self.storage_read_client);
        async move { Ok(client.update_to_latest_ledger_async(0, vec![]).await?.1) }.boxed()
    }

    fn execute_chunk(
        &self,
        txn_list_with_proof: TransactionListWithProof,
        ledger_info_with_sigs: LedgerInfoWithSignatures,
    ) -> Pin<Box<dyn Future<Output = Result<()>> + Send>> {
        convert_to_future(
            self.executor
                .execute_chunk(txn_list_with_proof, ledger_info_with_sigs),
        )
    }

    fn get_chunk(
        &self,
        known_version: u64,
        limit: u64,
        target: LedgerInfoWithSignatures,
    ) -> Pin<Box<dyn Future<Output = Result<GetChunkResponse>> + Send>> {
        let client = Arc::clone(&self.storage_read_client);
        async move {
            let transactions = client
                .get_transactions_async(
                    known_version + 1,
                    limit,
                    target.ledger_info().version(),
                    false,
                )
                .await?;
            if transactions.transaction_and_infos.is_empty() {
                error!(
                    "[state sync] can't get {} txns from version {}",
                    limit, known_version
                );
            }
            Ok(GetChunkResponse {
                ledger_info_with_sigs: Some(target.into()),
                txn_list_with_proof: Some(transactions.into()),
            })
        }
            .boxed()
    }

    fn validate_ledger_info(&self, target: &LedgerInfo) -> Result<()> {
        target.verify(&self.validator_verifier)?;
        Ok(())
    }
}


