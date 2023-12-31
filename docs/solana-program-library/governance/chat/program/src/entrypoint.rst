governance/chat/program/src/entrypoint.rs
=========================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    //! Program entrypoint
#![cfg(all(target_os = "solana", not(feature = "no-entrypoint")))]

use crate::{error::GovernanceChatError, processor};
use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult,
    program_error::PrintProgramError, pubkey::Pubkey,
};

entrypoint!(process_instruction);
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    if let Err(error) = processor::process_instruction(program_id, accounts, instruction_data) {
        // catch the error so we can print it
        error.print::<GovernanceChatError>();
        return Err(error);
    }
    Ok(())
}


