sdk/program/src/address_lookup_table_account.rs
===============================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! The definition of address lookup table accounts.
//!
//! As used by the [`v0` message format][v0].
//!
//! [v0]: crate::message::v0

use solana_program::pubkey::Pubkey;

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct AddressLookupTableAccount {
    pub key: Pubkey,
    pub addresses: Vec<Pubkey>,
}


