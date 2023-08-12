stealth/program/src/lib.rs
==========================

Last edited: 2022-04-29 15:13:47

Contents:

.. code-block:: rs

    
mod entrypoint;
pub mod processor;
pub mod state;
pub mod instruction;
pub mod error;
pub mod pod;

pub mod equality_proof;
pub mod transfer_proof;

// TODO: use spl-zk-token-sdk
pub mod errors;
pub mod encryption;
pub mod transcript;
pub mod zk_token_elgamal;

solana_program::declare_id!("privzjrXhtea8kKt3uE94X34AHaiLj2Vbwd51y3aUSi");


