program/src/entrypoint.rs
=========================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: rs

    use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult,
    program_error::PrintProgramError, pubkey::Pubkey,
};

use crate::{error::Crows, processor::Processor};

entrypoint!(process_instruction);
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    if let Err(error) = Processor::process_instruction(program_id, accounts, instruction_data) {
        // catch the error so we can print it
        error.print::<Crows>();
        return Err(error);
    }
    Ok(())
}


