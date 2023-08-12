program/src/lib.rs
==================

Last edited: 2023-04-22 23:05:55

Contents:

.. code-block:: rs

    pub mod entrypoint;
pub mod error;
pub mod instruction;
pub mod processor;
pub mod state;

pub use solana_program;

solana_program::declare_id!("MyProgram1111111111111111111111111111111111");


