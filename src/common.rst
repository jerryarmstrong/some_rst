src/common.rs
=============

Last edited: 2023-08-11 21:59:14

Contents:

.. code-block:: rs

    pub use std::{
    collections::HashMap,
    fs::File,
    path::{Path, PathBuf},
    str::FromStr,
};

pub use anchor_client::{
    solana_sdk::{
        commitment_config::CommitmentConfig,
        pubkey::Pubkey,
        signature::{Keypair, Signature, Signer},
        system_instruction, system_program, sysvar,
        transaction::Transaction,
    },
    Client, Program,
};
pub use anchor_lang::AccountDeserialize;
pub use anyhow::{anyhow, Result};
pub use bs58;
pub use indexmap::IndexMap;
pub use mpl_candy_machine_core::{
    accounts as nft_accounts, instruction as nft_instruction, CandyMachine,
};
pub use reqwest::{Client as HttpClient, Response};
pub use serde::Deserialize;
pub use serde_json::{json, Value};
pub use tracing::{debug, error, info, warn};

pub use crate::{
    cache::{Cache, CacheItem},
    constants::*,
    errors::*,
    parse::path_to_string,
    setup::{setup_client, sugar_setup},
};


