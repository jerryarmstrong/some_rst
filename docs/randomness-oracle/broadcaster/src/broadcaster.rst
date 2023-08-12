broadcaster/src/broadcaster.rs
==============================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use rand::Rng;
use randomness_oracle_program::{id, instruction, state::RandomnessOracle};
use solana_client::{client_error::ClientError, rpc_client::RpcClient};
use solana_program::pubkey::Pubkey;
use solana_sdk::{
    signature::{Keypair, Signature},
    signer::Signer,
    transaction::Transaction,
};
use std::error::Error;
use tokio::task::JoinHandle;

pub struct Broadcaster {
    pub rpc_url: String,
    pub authority: Keypair,
}

impl Broadcaster {
    pub fn new(rpc_url: String, authority: Keypair) -> Self {
        Self { rpc_url, authority }
    }

    pub async fn broadcast(
        &self,
        accounts: Vec<(Pubkey, RandomnessOracle)>,
    ) -> Result<Vec<Signature>, Box<dyn Error>> {
        let mut signatures = vec![];
        let mut rng = rand::thread_rng();

        for (pubkey, _) in accounts {
            let rpc_url = self.rpc_url.clone();
            let authority = Keypair::from_bytes(&self.authority.to_bytes()[..]).unwrap();
            let value: [u8; 32] = rng.gen();

            let handle: JoinHandle<Result<Signature, ClientError>> = tokio::spawn(async move {
                let rpc_client = RpcClient::new(rpc_url);

                update_randomness_oracle(&rpc_client, &pubkey, &authority, value)
            });

            let signature = handle.await.ok();

            if let Some(signature) = signature {
                signatures.push(signature?);
            } else {
                return Err("Error while send tx".into());
            }
        }

        Ok(signatures)
    }
}

fn update_randomness_oracle(
    rpc_client: &RpcClient,
    pubkey: &Pubkey,
    authority: &Keypair,
    value: [u8; 32],
) -> Result<Signature, ClientError> {
    let mut tx = Transaction::new_with_payer(
        &[instruction::update_randomness_oracle(
            &id(),
            pubkey,
            &authority.pubkey(),
            value,
        )],
        Some(&authority.pubkey()),
    );

    let (recent_blockhash, _) = rpc_client.get_recent_blockhash()?;

    tx.try_sign(&[authority], recent_blockhash)?;

    rpc_client.send_transaction(&tx)
}


