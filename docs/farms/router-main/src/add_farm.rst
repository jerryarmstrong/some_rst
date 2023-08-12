router-main/src/add_farm.rs
===========================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    //! Saves Farm's metadata on-chain

use {
    crate::refdb_init::{check_or_init_refdb, check_or_init_refdb_target},
    solana_farm_sdk::{farm::Farm, refdb, refdb::RefDB, traits::Packed},
    solana_program::{
        account_info::{next_account_info, AccountInfo},
        entrypoint::ProgramResult,
        msg,
        pubkey::Pubkey,
    },
};

pub fn add_farm(program_id: &Pubkey, accounts: &[AccountInfo], farm: &Farm) -> ProgramResult {
    msg!("Processing MainInstruction::AddFarm {}", farm.name);

    // validate accounts
    let accounts_iter = &mut accounts.iter();

    let signer_account = next_account_info(accounts_iter)?;
    let _multisig_account = next_account_info(accounts_iter)?;
    let refdb_account = next_account_info(accounts_iter)?;
    let target_account = next_account_info(accounts_iter)?;

    check_or_init_refdb(
        program_id,
        signer_account,
        refdb_account,
        refdb::StorageType::Farm,
        0,
        false,
    )?;
    check_or_init_refdb_target(
        program_id,
        signer_account,
        target_account,
        refdb::StorageType::Farm,
        &farm.name,
        farm.get_size(),
        false,
    )?;

    // update refdb storage
    msg!("Updating refdb storage");
    RefDB::write(
        *refdb_account.try_borrow_mut_data()?,
        &refdb::Record {
            index: farm.refdb_index,
            counter: farm.refdb_counter,
            tag: refdb::StorageType::Farm as u16,
            name: farm.name,
            reference: refdb::Reference::Pubkey {
                data: *target_account.key,
            },
        },
    )?;

    // fill in data
    msg!("Writing metadata account");
    farm.pack(*target_account.try_borrow_mut_data()?)?;

    msg!("AddFarm complete");

    Ok(())
}


