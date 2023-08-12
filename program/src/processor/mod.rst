program/src/processor/mod.rs
============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use crate::{
    errors::MigrationError,
    instruction::{MigrationInstruction, UpdateArgs},
    state::{MigrationState, ProgramSigner, UnlockMethod, SPL_TOKEN_ID},
};
use borsh::{BorshDeserialize, BorshSerialize};
use mpl_token_metadata::{
    instruction::{builders::MigrateBuilder, InstructionBuilder, MigrateArgs},
    state::{Metadata, MigrationType, TokenMetadataAccount, EDITION, PREFIX},
};
use mpl_utils::{assert_derivation, assert_owned_by, assert_signer};
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    clock::Clock,
    entrypoint::ProgramResult,
    program::invoke_signed,
    program_error::ProgramError,
    program_memory::sol_memcpy,
    program_option::COption,
    pubkey::Pubkey,
    sysvar::{self, Sysvar},
};

use spl_token::state::Account as TokenAccount;

mod close;
mod initialize;
mod migrate;
mod misc;
mod start;
mod update;
mod validators;

use close::close_migration_state;
use migrate::migrate_item;
use misc::init_signer;
use start::start_migration;
use update::update_state;
use validators::*;

pub struct Processor;
impl Processor {
    pub fn process_instruction<'a>(
        program_id: &'a Pubkey,
        accounts: &'a [AccountInfo<'a>],
        instruction_data: &[u8],
    ) -> ProgramResult {
        let instruction: MigrationInstruction =
            MigrationInstruction::try_from_slice(instruction_data)?;

        match instruction {
            MigrationInstruction::Initialize(_args) => {
                Err(MigrationError::DeprecatedInstruction.into())
            }
            MigrationInstruction::Update(args) => update_state(program_id, accounts, args),
            MigrationInstruction::Close => close_migration_state(program_id, accounts),
            MigrationInstruction::Start => start_migration(program_id, accounts),
            MigrationInstruction::Migrate => migrate_item(program_id, accounts),
            MigrationInstruction::InitSigner => init_signer(program_id, accounts),
        }
    }
}


