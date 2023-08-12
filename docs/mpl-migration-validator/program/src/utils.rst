program/src/utils.rs
====================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use mpl_token_metadata::{
    assertions::collection::assert_is_collection_delegated_authority,
    state::{CollectionAuthorityRecord, Metadata},
};
use solana_program::{
    account_info::AccountInfo, entrypoint::ProgramResult, program_error::ProgramError,
    pubkey::Pubkey, system_program,
};

use crate::{errors::MigrationError, state::MigrationState, PROGRAM_SIGNER};

pub fn assert_valid_delegate(
    delegate_pubkey: &Pubkey,
    delegate_record_info: &AccountInfo,
    collection_metadata: &Metadata,
    migration_state: &MigrationState,
) -> Result<(), ProgramError> {
    let info = &migration_state.collection_info;
    // Mint is the correct one for the metadata account.
    if collection_metadata.mint != info.mint {
        return Err(MigrationError::MetadataMintMistmatch.into());
    }

    if collection_metadata.update_authority != info.authority {
        return Err(MigrationError::InvalidAuthority.into());
    }

    let bump = assert_is_collection_delegated_authority(
        delegate_record_info,
        delegate_pubkey,
        &info.mint,
    )?;

    let data = delegate_record_info.try_borrow_data()?;
    if data.len() == 0 {
        return Err(MigrationError::InvalidDelegate.into());
    }

    let record = CollectionAuthorityRecord::from_bytes(&data)?;

    if record.bump != bump {
        return Err(MigrationError::InvalidDelegate.into());
    }

    if let Some(update_authority) = record.update_authority {
        if update_authority != collection_metadata.update_authority {
            return Err(MigrationError::InvalidDelegate.into());
        }
    } else {
        return Err(MigrationError::InvalidDelegate.into());
    }

    Ok(())
}

pub fn close_program_account<'a>(
    account_info: &AccountInfo<'a>,
    funds_dest_account_info: &AccountInfo<'a>,
) -> ProgramResult {
    // Transfer lamports from the account to the destination account.
    let dest_starting_lamports = funds_dest_account_info.lamports();
    **funds_dest_account_info.lamports.borrow_mut() = dest_starting_lamports
        .checked_add(account_info.lamports())
        .unwrap();
    **account_info.lamports.borrow_mut() = 0;

    // Realloc the account data size to 0 bytes and teassign ownership of
    // the account to the system program
    account_info.realloc(0, false)?;
    account_info.assign(&system_program::ID);

    Ok(())
}

pub fn find_migration_state_pda(mint: &Pubkey) -> (Pubkey, u8) {
    let seeds = &[b"migration", mint.as_ref()];
    Pubkey::find_program_address(seeds, &crate::ID)
}

pub fn find_delegate_record_pda(mint: &Pubkey) -> (Pubkey, u8) {
    let seeds = &[
        mpl_token_metadata::state::PREFIX.as_bytes(),
        mpl_token_metadata::ID.as_ref(),
        mint.as_ref(),
        mpl_token_metadata::pda::COLLECTION_AUTHORITY.as_bytes(),
        PROGRAM_SIGNER.as_ref(),
    ];
    Pubkey::find_program_address(seeds, &mpl_token_metadata::ID)
}


