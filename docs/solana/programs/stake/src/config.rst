programs/stake/src/config.rs
============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! config for staking
//!  carries variables that the stake program cares about
#[deprecated(
    since = "1.8.0",
    note = "Please use `solana_sdk::stake::config` or `solana_program::stake::config` instead"
)]
pub use solana_sdk::stake::config::*;
#[allow(deprecated)]
use solana_sdk::stake::config::{self, Config};
use {
    bincode::deserialize,
    solana_config_program::{create_config_account, get_config_data},
    solana_sdk::{
        account::{AccountSharedData, ReadableAccount, WritableAccount},
        genesis_config::GenesisConfig,
        transaction_context::BorrowedAccount,
    },
};

#[allow(deprecated)]
pub fn from(account: &BorrowedAccount) -> Option<Config> {
    get_config_data(account.get_data())
        .ok()
        .and_then(|data| deserialize(data).ok())
}

#[allow(deprecated)]
pub fn create_account(lamports: u64, config: &Config) -> AccountSharedData {
    create_config_account(vec![], config, lamports)
}

#[allow(deprecated)]
pub fn add_genesis_account(genesis_config: &mut GenesisConfig) -> u64 {
    let mut account = create_config_account(vec![], &Config::default(), 0);
    let lamports = genesis_config.rent.minimum_balance(account.data().len());

    account.set_lamports(lamports.max(1));

    genesis_config.add_account(config::id(), account);

    lamports
}


