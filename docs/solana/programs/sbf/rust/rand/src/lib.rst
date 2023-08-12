programs/sbf/rust/rand/src/lib.rs
=================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Example Rust-based SBF program that tests rand behavior

#![allow(unreachable_code)]

extern crate solana_program;
use solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, msg, pubkey::Pubkey};

solana_program::entrypoint!(process_instruction);
#[allow(clippy::unnecessary_wraps)]
fn process_instruction(
    _program_id: &Pubkey,
    _accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    msg!("rand");
    Ok(())
}


