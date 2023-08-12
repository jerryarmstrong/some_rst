broadcaster/src/utils.rs
========================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use randomness_oracle_program::{id, state::AccountType};
use solana_account_decoder::UiAccountEncoding;
use solana_client::{
    client_error::ClientError,
    rpc_client::RpcClient,
    rpc_config::{RpcAccountInfoConfig, RpcProgramAccountsConfig},
    rpc_filter::{Memcmp, MemcmpEncodedBytes, MemcmpEncoding, RpcFilterType},
};
use solana_program::pubkey::Pubkey;
use solana_sdk::{account::Account, signature::Keypair};

pub struct Config {
    pub rpc_url: String,
    pub verbose: bool,
    pub authority: Keypair,
}

pub fn get_program_accounts(
    rpc_client: &RpcClient,
    account_type: AccountType,
    pubkey: &Pubkey,
) -> Result<Vec<(Pubkey, Account)>, ClientError> {
    rpc_client.get_program_accounts_with_config(
        &id(),
        RpcProgramAccountsConfig {
            filters: Some(vec![
                // Account type
                RpcFilterType::Memcmp(Memcmp {
                    offset: 0,
                    bytes: MemcmpEncodedBytes::Binary(
                        bs58::encode([account_type as u8]).into_string(),
                    ),
                    encoding: Some(MemcmpEncoding::Binary),
                }),
                // Account parent
                RpcFilterType::Memcmp(Memcmp {
                    offset: 1,
                    bytes: MemcmpEncodedBytes::Binary(pubkey.to_string()),
                    encoding: Some(MemcmpEncoding::Binary),
                }),
            ]),
            account_config: RpcAccountInfoConfig {
                encoding: Some(UiAccountEncoding::Base64Zstd),
                ..RpcAccountInfoConfig::default()
            },
            ..RpcProgramAccountsConfig::default()
        },
    )
}


