src/config.rs
=============

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use anyhow::{anyhow, Result};
use dirs::home_dir;
use serde::{Deserialize, Serialize};
use solana_client::rpc_client::RpcClient;
use solana_program::pubkey::Pubkey;
use solana_sdk::{
    clock::Slot,
    commitment_config::CommitmentConfig,
    hash::Hash,
    signature::{read_keypair_file, Keypair},
};
use std::{env, fs::File, path::PathBuf, str::FromStr};

#[derive(Debug, Deserialize, Serialize)]
struct SolanaConfig {
    pub json_rpc_url: String,
    pub keypair_path: String,
    pub commitment: String,
}

pub struct CliConfig {
    pub client: RpcClient,
    pub keypair: Keypair,
    pub recent_blockhash: Hash,
    pub recent_slot: Slot,
    pub realm_id: Pubkey,
    pub governance_id: Pubkey,
}

#[derive(Debug, Default)]
pub struct CliConfigBuilder {
    pub json_rpc_url: Option<String>,
    pub keypair_path: Option<PathBuf>,
    pub commitment: Option<String>,
}

impl CliConfigBuilder {
    pub fn new() -> Self {
        Self {
            json_rpc_url: None,
            keypair_path: None,
            commitment: None,
        }
    }
    pub fn rpc_url(mut self, json_rpc_url: String) -> Self {
        self.json_rpc_url = Some(json_rpc_url);
        self
    }
    pub fn keypair_path(mut self, keypair_path: PathBuf) -> Self {
        self.keypair_path = Some(keypair_path);
        self
    }
    pub fn commitment(mut self, commitment: String) -> Self {
        self.commitment = Some(commitment);
        self
    }
    pub fn build(&self) -> Result<CliConfig> {
        let rpc_url = self
            .json_rpc_url
            .clone()
            .ok_or_else(|| anyhow!("No rpc url provided"))?;

        let commitment = match self.commitment.clone() {
            Some(commitment) => CommitmentConfig::from_str(&commitment)?,
            None => CommitmentConfig::confirmed(),
        };

        let client = RpcClient::new_with_commitment(rpc_url, commitment);

        let keypair_path = self
            .keypair_path
            .clone()
            .ok_or_else(|| anyhow!("No keypair path provided"))?;

        let keypair =
            read_keypair_file(keypair_path).map_err(|_| anyhow!("Unable to read keypair file"))?;

        let recent_blockhash = client.get_latest_blockhash()?;
        let recent_slot = client.get_slot()?;

        let realm_id_var =
            env::var("REALM_ID").map_err(|_| anyhow!("Missing REALM_ID env var."))?;
        let governance_id_var =
            env::var("GOVERNANCE_ID").map_err(|_| anyhow!("Missing GOVERNANCE_ID env var."))?;

        let realm_id = Pubkey::from_str(&realm_id_var)?;
        let governance_id = Pubkey::from_str(&governance_id_var)?;

        Ok(CliConfig {
            client,
            keypair,
            recent_blockhash,
            recent_slot,
            realm_id,
            governance_id,
        })
    }
}

impl CliConfig {
    pub fn new(keypair_path: Option<PathBuf>, rpc_url: Option<String>) -> Result<Self> {
        let mut builder = CliConfigBuilder::new();
        let solana_config = parse_solana_config();

        if let Some(config) = solana_config {
            builder = builder
                .rpc_url(config.json_rpc_url)
                .keypair_path(config.keypair_path.into())
                .commitment(config.commitment);
        }

        if let Some(keypair_path) = keypair_path {
            builder = builder.keypair_path(keypair_path);
        }

        if let Some(rpc_url) = rpc_url {
            builder = builder.rpc_url(rpc_url);
        }

        let config = builder.build()?;

        Ok(config)
    }
}

fn parse_solana_config() -> Option<SolanaConfig> {
    let home_path = home_dir().expect("Couldn't find home dir");

    let solana_config_path = home_path
        .join(".config")
        .join("solana")
        .join("cli")
        .join("config.yml");

    let config_file = File::open(solana_config_path).ok();

    if let Some(config_file) = config_file {
        let config: SolanaConfig = serde_yaml::from_reader(config_file).ok()?;
        return Some(config);
    }
    None
}


