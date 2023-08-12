src/entrypoint.rs
=================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    #![cfg(all(target_arch = "bpf", not(feature = "no-entrypoint")))]

use crate::api::{Action, DigitalAssetProtocolError};
use solana_program::{
    account_info::AccountInfo,
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

use thiserror::Error;

entrypoint!(process_instruction);
fn process_instruction<'info>(
    program_id: &Pubkey,
    accounts: &'info [AccountInfo<'info>],
    instruction_data: &'info [u8],
) -> ProgramResult {
    let mut action = Action::from_instruction(
        program_id,
        accounts,
        instruction_data,
    )?;
    action.run()?;
    /*

    Digital Asset
        Standards
            Lifecycle Actions: Create, Delete
            Modules



        Modules -> Enforce Valid Data Stored ina  Blob
            Data -> {
                [Key]: value
            }
            Ownership -> {
                 OwnershipModel
                 Address: Pubkey
            }

        Blob is a bit of validateable data

           NFT Standard
            create, transfer, delete

            Ownership
            Data
            Royalty
            Creators
            Governance

          Identity NFT Standard

    */
    msg!("{:?}",action.standard);
    Ok(())
}




