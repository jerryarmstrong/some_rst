programs/sbf/rust/upgradeable/src/lib.rs
========================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Example Rust-based SBF upgradeable program

extern crate solana_program;
use solana_program::{
    account_info::AccountInfo, entrypoint::ProgramResult, msg, pubkey::Pubkey, sysvar::clock,
};

solana_program::entrypoint!(process_instruction);
fn process_instruction(
    _program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    msg!("Upgradeable program");
    assert_eq!(accounts.len(), 1);
    assert_eq!(*accounts[0].key, clock::id());
    Err(42.into())
}


