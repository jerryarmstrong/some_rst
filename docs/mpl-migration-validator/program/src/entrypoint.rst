program/src/entrypoint.rs
=========================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult,
    program_error::PrintProgramError, pubkey::Pubkey,
};

use crate::{errors::*, processor::Processor};

entrypoint!(process_instruction);
fn process_instruction<'a>(
    program_id: &'a Pubkey,
    accounts: &'a [AccountInfo<'a>],
    instruction_data: &[u8],
) -> ProgramResult {
    if let Err(error) = Processor::process_instruction(program_id, accounts, instruction_data) {
        // catch the error so we can print it
        error.print::<MigrationError>();
        return Err(error);
    }
    Ok(())
}


