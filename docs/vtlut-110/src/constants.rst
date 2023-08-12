src/constants.rs
================

Last edited: 2022-10-31 20:56:14

Contents:

.. code-block:: rs

    use solana_program::{pubkey, pubkey::Pubkey};

/// Address lookup table program ID
pub const ADDRESS_LOOKUP_TABLE_ID: Pubkey = pubkey!("AddressLookupTab1e1111111111111111111111111");

/// The maximum number of addresses that a lookup table can hold
pub const LOOKUP_TABLE_MAX_ADDRESSES: usize = 256;

/// The serialized size of lookup table metadata
pub const LOOKUP_TABLE_META_SIZE: usize = 56;


