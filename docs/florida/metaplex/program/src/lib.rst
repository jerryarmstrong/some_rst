metaplex/program/src/lib.rs
===========================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: rs

    //! A Metaplex Store program for the Solana blockchain.

pub mod deprecated_state;
pub mod entrypoint;
pub mod error;
pub mod instruction;
pub mod processor;
pub mod state;
pub mod utils;
// Export current sdk types for downstream users building with a different sdk version
pub use solana_program;

solana_program::declare_id!("p1exdMJcjVao65QdewkaZRUnU6VPSXhus9n2GzWfh98");


