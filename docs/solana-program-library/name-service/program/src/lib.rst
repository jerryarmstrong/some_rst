name-service/program/src/lib.rs
===============================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    #[cfg(not(feature = "no-entrypoint"))]
pub mod entrypoint;
pub mod error;
pub mod instruction;
pub mod processor;
pub mod state;

// Export current sdk types for downstream users building with a different sdk version
pub use solana_program;

solana_program::declare_id!("namesLPneVptA9Z5rqUDD9tMTWEJwofgaYwp8cawRkX");


