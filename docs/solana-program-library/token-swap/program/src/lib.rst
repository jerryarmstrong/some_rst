token-swap/program/src/lib.rs
=============================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    #![deny(missing_docs)]

//! An Uniswap-like program for the Solana blockchain.

pub mod constraints;
pub mod curve;
pub mod error;
pub mod instruction;
pub mod processor;
pub mod state;

#[cfg(not(feature = "no-entrypoint"))]
mod entrypoint;

// Export current sdk types for downstream users building with a different sdk version
pub use solana_program;

solana_program::declare_id!("SwapsVeCiPHMUAtzQWZw7RjsKjgCjhwU55QGu4U1Szw");


