sdk/cargo-build-sbf/tests/crates/fail/src/lib.rs
================================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Example Rust-based SBF noop program

use solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, pubkey::Pubkey};

solana_program::entrypoint!(process_instruction);
fn process_instruction(
    _program_id: &Pubkey,
    _accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // error to make build fail: no return value
}


