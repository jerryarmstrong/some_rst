src/main.rs
===========

Last edited: 2022-05-22 02:11:20

Contents:

.. code-block:: rs

    use anyhow::{anyhow, Result};
use borsh::BorshDeserialize;
use futures::future::select_all;
use metaboss_lib::derive::derive_metadata_pda;
use mpl_token_metadata::state::{Collection, Metadata};
use serde::{Deserialize, Serialize};
use solana_client::rpc_client::RpcClient;
use solana_sdk::{commitment_config::CommitmentConfig, pubkey::Pubkey};
use std::{
    cmp, collections::HashMap, env, fs::File, path::Path, str::FromStr, sync::Arc, time::Duration,
};

const PARALLEL_LIMIT: usize = 50;

#[tokio::main]
async fn main() -> Result<()> {
    let args = env::args().collect::<Vec<_>>();

    println!("Getting solana config");
    let sol_config = parse_solana_config();
    let sol_config = sol_config.ok_or_else(|| anyhow!("Failed to parse solana config"))?;

    let commitment = CommitmentConfig::from_str(&sol_config.commitment)?;
    let timeout = Duration::from_secs(300);
    let client = Arc::new(RpcClient::new_with_timeout_and_commitment(
        sol_config.json_rpc_url.clone(),
        timeout,
        commitment,
    ));

    println!("Getting mint list");
    let mint_list_path = args[1].clone();
    let mint_list_name = mint_list_path.split('.').next().unwrap().to_string();

    let f = File::open(mint_list_path)?;
    let mut mint_list: Vec<String> = serde_json::from_reader(f)?;

    let mut collections: HashMap<String, Vec<String>> = HashMap::new();

    let mut handles = Vec::new();
    let mut errors = Vec::new();

    println!("Looping over mint addresses");
    for mint in mint_list.drain(0..cmp::min(mint_list.len(), PARALLEL_LIMIT)) {
        println!("Getting mint metadata for {}", mint);
        let client = client.clone();
        handles.push(tokio::spawn(async move {
            get_mint_collection(&client, mint.to_string()).await
        }));
    }

    while !handles.is_empty() {
        match select_all(handles).await {
            (Ok(res), _index, remaining) => {
                handles = remaining;

                if res.is_ok() {
                    let (mint, collection_opt) = res.unwrap();
                    match collection_opt {
                        Some(collection) => {
                            collections
                                .entry(collection.key.to_string())
                                .or_insert_with(Vec::new)
                                .push(mint.to_string());
                        }
                        None => {
                            collections
                                .entry("none".to_string())
                                .or_insert_with(Vec::new)
                                .push(mint.to_string());
                        }
                    }
                } else {
                    errors.push(res.err().unwrap());
                }
            }
            (Err(err), _index, remaining) => {
                errors.push(err.into());
                // ignoring all errors
                handles = remaining;
            }
        }

        if !mint_list.is_empty() {
            // if we are half way through, let spawn more transactions
            if (PARALLEL_LIMIT - handles.len()) > (PARALLEL_LIMIT / 2) {
                // syncs cache (checkpoint)

                for mint in mint_list.drain(0..cmp::min(mint_list.len(), PARALLEL_LIMIT)) {
                    println!("Getting mint metadata for {}", mint);
                    let client = client.clone();
                    handles.push(tokio::spawn(async move {
                        get_mint_collection(&client, mint.to_string()).await
                    }));
                }
            }
        }
    }

    let out = File::create(format!("{}-collections.json", mint_list_name))?;
    serde_json::to_writer(out, &collections)?;

    Ok(())
}

async fn get_mint_collection<'a>(
    client: &RpcClient,
    mint: String,
) -> Result<(String, Option<Collection>)> {
    let mint_pubkey = Pubkey::from_str(&mint)?;
    let metadata_pubkey = derive_metadata_pda(&mint_pubkey);
    let data = client.get_account_data(&metadata_pubkey)?;
    let md = Metadata::deserialize(&mut data.as_slice())?;

    Ok((mint, md.collection))
}

#[derive(Debug, Deserialize, Serialize)]
pub struct SolanaConfig {
    pub json_rpc_url: String,
    pub keypair_path: String,
    pub commitment: String,
}

pub fn parse_solana_config() -> Option<SolanaConfig> {
    let home = if cfg!(unix) {
        env::var_os("HOME").expect("Coulnd't find UNIX home key.")
    } else if cfg!(windows) {
        let drive = env::var_os("HOMEDRIVE").expect("Coulnd't find Windows home drive key.");
        let path = env::var_os("HOMEPATH").expect("Coulnd't find Windows home path key.");
        Path::new(&drive).join(&path).as_os_str().to_owned()
    } else if cfg!(target_os = "macos") {
        env::var_os("HOME").expect("Coulnd't find MacOS home key.")
    } else {
        panic!("Unsupported OS!");
    };

    let config_path = Path::new(&home)
        .join(".config")
        .join("solana")
        .join("cli")
        .join("config.yml");

    let conf_file = match File::open(config_path) {
        Ok(f) => f,
        Err(_) => return None,
    };
    serde_yaml::from_reader(&conf_file).ok()
}


