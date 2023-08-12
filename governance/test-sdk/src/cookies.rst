governance/test-sdk/src/cookies.rs
==================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    use solana_program::pubkey::Pubkey;
use solana_sdk::account::Account;

#[derive(Debug)]
pub struct TokenAccountCookie {
    pub address: Pubkey,
}

#[derive(Debug)]
pub struct WalletCookie {
    pub address: Pubkey,
    pub account: Account,
}


