broadcaster/src/subscriber.rs
=============================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use crate::{broadcaster::*, utils::get_program_accounts};
use randomness_oracle_program::state::{AccountType, RandomnessOracle};
use solana_client::rpc_client::RpcClient;
use solana_program::{clock::Slot, program_pack::Pack, pubkey::Pubkey};
use solana_sdk::signer::Signer;
use std::sync::{
    atomic::{AtomicBool, Ordering},
    Arc,
};
use std::{thread, time};

pub const SLEEP_TIME: time::Duration = time::Duration::from_secs(5);

pub struct Subscriber {
    rpc_url: String,
}

impl Subscriber {
    pub fn new(rpc_url: String) -> Self {
        Self { rpc_url }
    }

    pub async fn run(&self, broadcaster: &Broadcaster) -> anyhow::Result<()> {
        let exit = Arc::new(AtomicBool::new(false));
        let mut current_slot: Option<Slot> = None;
        let mut rpc_client = RpcClient::new(broadcaster.rpc_url.clone());

        loop {
            if exit.load(Ordering::Relaxed) {
                eprintln!("exit");
                break;
            }

            let request = rpc_client.get_slot();

            match request {
                Ok(new_slot) => {
                    let received_slot = new_slot as u64;

                    match current_slot {
                        Some(value) => {
                            if received_slot <= value {
                                continue;
                            }

                            let accounts: Vec<(Pubkey, RandomnessOracle)> = get_program_accounts(
                                &rpc_client,
                                AccountType::RandomnessOracle,
                                &broadcaster.authority.pubkey(),
                            )?
                            .into_iter()
                            .filter_map(|(address, account)| {
                                match RandomnessOracle::unpack_unchecked(&account.data) {
                                    Ok(pool) => Some((address, pool)),
                                    _ => None,
                                }
                            })
                            .collect();

                            println!(
                                "Latest stable block: {}, Pending block: {}, Total accounts: {}",
                                received_slot,
                                received_slot - value,
                                accounts.len(),
                            );

                            let signatures = broadcaster.broadcast(accounts).await.ok();

                            if let Some(signatures) = signatures {
                                println!("{:?}", signatures);

                                current_slot = Some(received_slot);
                            } else {
                                eprintln!(
                                    "Broadcaster was disconnected while was sending transaction"
                                );
                                continue;
                            }
                        }
                        _ => current_slot = Some(received_slot),
                    };
                }
                Err(err) => {
                    eprintln!("disconnected: {}", err);
                    thread::sleep(SLEEP_TIME);
                    rpc_client = RpcClient::new(broadcaster.rpc_url.clone());
                }
            }
        }

        Ok(())
    }
}


