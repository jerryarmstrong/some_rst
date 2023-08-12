src/utils.rs
============

Last edited: 2023-06-13 21:53:04

Contents:

.. code-block:: rs

    use std::{str::FromStr, time::Duration};

use anyhow::{bail, Result};
use indicatif::{ProgressBar, ProgressStyle};
use serde::Deserialize;
use serde_json::json;
use solana_client::{rpc_client::RpcClient, rpc_request::RpcRequest};
use solana_program::{pubkey, pubkey::Pubkey};
use solana_sdk::hash::Hash;

use crate::Cluster;

const TOKEN_METADATA_ID: Pubkey = pubkey!("metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s");

// Hash for devnet cluster
pub const DEVNET_HASH: &str = "EtWTRABZaYq6iMfeYKouRu166VU2xqa1wcaWoxPkrZBG";

/// Hash for mainnet-beta cluster
pub const MAINNET_HASH: &str = "5eykt4UsFv8P8NJdTREpY1vzqKqZKvdpKuc147dw2N9d";

pub fn find_metadata_pda(mint: &Pubkey) -> (Pubkey, u8) {
    let seeds = &[b"metadata", TOKEN_METADATA_ID.as_ref(), mint.as_ref()];
    Pubkey::find_program_address(seeds, &TOKEN_METADATA_ID)
}

pub fn find_migrate_state_pda(mint: &Pubkey) -> (Pubkey, u8) {
    let seeds = &[b"migration", mint.as_ref()];
    Pubkey::find_program_address(seeds, &mpl_migration_validator::ID)
}

pub fn find_program_signer_pda() -> (Pubkey, u8) {
    Pubkey::find_program_address(&[b"signer"], &mpl_migration_validator::ID)
}

pub fn get_cluster(rpc_client: &RpcClient) -> Result<Cluster> {
    let devnet_hash = Hash::from_str(DEVNET_HASH).unwrap();
    let mainnet_hash = Hash::from_str(MAINNET_HASH).unwrap();
    let genesis_hash = rpc_client.get_genesis_hash()?;

    Ok(if genesis_hash == devnet_hash {
        Cluster::Devnet
    } else if genesis_hash == mainnet_hash {
        Cluster::Mainnet
    } else {
        return Err(anyhow::anyhow!("Unknown or unsupported cluster"));
    })
}

pub fn spinner_with_style() -> ProgressBar {
    let pb = ProgressBar::new_spinner();
    pb.enable_steady_tick(Duration::from_millis(100));
    pb.set_style(
        ProgressStyle::default_spinner()
            .tick_strings(&[
                "▹▹▹▹▹",
                "▸▹▹▹▹",
                "▹▸▹▹▹",
                "▹▹▸▹▹",
                "▹▹▹▸▹",
                "▹▹▹▹▸",
                "▪▪▪▪▪",
            ])
            .template("{spinner:.dim} {msg}")
            .expect("failed to set progressbar template"),
    );
    pb
}

pub fn get_nft_token_account(client: &RpcClient, mint: Pubkey) -> Result<Pubkey> {
    let request = RpcRequest::Custom {
        method: "getTokenLargestAccounts",
    };
    let params = json!([mint.to_string(), { "commitment": "confirmed" }]);
    let result: JRpcResponse = client.send(request, params)?;

    let token_accounts: Vec<TokenAccount> = result
        .value
        .into_iter()
        .filter(|account| account.amount.parse::<u64>().unwrap() == 1)
        .collect();

    if token_accounts.len() > 1 {
        bail!(
            "Mint account {} had more than one token account with 1 token",
            mint
        );
    }

    if token_accounts.is_empty() {
        bail!("Mint account {} had zero token accounts with 1 token", mint);
    }

    let token_pubkey = Pubkey::from_str(&token_accounts[0].address)?;

    Ok(token_pubkey)
}

#[derive(Debug, Deserialize)]
pub struct JRpcResponse {
    value: Vec<TokenAccount>,
}

#[derive(Debug, Deserialize)]
struct TokenAccount {
    address: String,
    amount: String,
    // decimals: u8,
    // #[serde(rename = "uiAmount")]
    // ui_amount: f32,
    // #[serde(rename = "uiAmountString")]
    // ui_amount_string: String,
}

pub fn create_progress_bar(msg: &'static str, len: u64) -> ProgressBar {
    let pb = ProgressBar::new(len);

    let style = ProgressStyle::default_bar()
        .template("{spinner:.blue} {msg} {wide_bar:.cyan/blue} {pos:>7}/{len:7} {eta_precise}")
        .unwrap()
        .progress_chars("##-");

    pb.set_style(style);
    pb.set_message(msg);
    pb
}


