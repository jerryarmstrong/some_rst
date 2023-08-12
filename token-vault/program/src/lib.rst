token-vault/program/src/lib.rs
==============================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: rs

    //! A Token Fraction program for the Solana blockchain.

pub mod entrypoint;
pub mod error;
pub mod instruction;
pub mod processor;
pub mod state;
pub mod utils;
// Export current sdk types for downstream users building with a different sdk version
pub use solana_program;

solana_program::declare_id!("vau1zxA2LbssAUEF7Gpw91zMM1LvXrvpzJtmZ58rPsn");


