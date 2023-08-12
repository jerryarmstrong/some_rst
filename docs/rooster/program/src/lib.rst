program/src/lib.rs
==================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: rs

    use crate::{error::Crows, instruction::RoosterCommand};
use borsh::{BorshDeserialize, BorshSerialize};
use mpl_token_metadata::instruction::{
    builders::TransferBuilder, InstructionBuilder, TransferArgs,
};
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint::ProgramResult,
    instruction::{AccountMeta, Instruction},
    msg,
    program_error::ProgramError,
    program_memory::sol_memcpy,
    pubkey,
    pubkey::Pubkey,
};

pub mod assertions;
#[cfg(not(feature = "no-entrypoint"))]
pub mod entrypoint;
pub mod error;
pub mod instruction;
pub mod pda;
pub mod processor;
pub mod state;

pub use mpl_token_metadata::{processor::AuthorizationData, state::TokenDelegateRole};

solana_program::declare_id!("Roostrnex2Z9Y2XZC49sFAdZARP8E4iFpEnZC5QJWdz");

pub const SPL_ATA_TOKEN_PROGRAM_ID: Pubkey =
    pubkey!("ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL");
pub const MPL_TOKEN_AUTH_RULES_PROGRAM_ID: Pubkey =
    pubkey!("auth9SigNpDKz4sJJ1DfCTuZrZNSAgh9sFD3rboVmgg");


