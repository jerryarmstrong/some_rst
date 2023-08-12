router-main/src/entrypoint.rs
=============================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Program entrypoint

#![cfg(not(feature = "no-entrypoint"))]

solana_security_txt::security_txt! {
    name: "Solana Farms",
    project_url: "https://github.com/solana-labs/farms",
    contacts: "email:solana.farms@protonmail.com",
    policy: "",
    preferred_languages: "en",
    auditors: "Halborn"
}

use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult, pubkey::Pubkey,
};

entrypoint!(process_instruction);
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    crate::processor::process_instruction(program_id, accounts, instruction_data)
}


