program/src/processor/start.rs
==============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use mpl_token_metadata::state::CollectionAuthorityRecord;

use crate::PROGRAM_SIGNER;

use super::*;

pub fn start_migration(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Fetch accounts
    let account_info_iter = &mut accounts.iter();
    let payer_info = next_account_info(account_info_iter)?;
    let authority_info = next_account_info(account_info_iter)?;
    let collection_mint_info = next_account_info(account_info_iter)?;
    let collection_metadata_info = next_account_info(account_info_iter)?;
    let delegate_info = next_account_info(account_info_iter)?;
    let delegate_record_info = next_account_info(account_info_iter)?;
    let migration_state_info = next_account_info(account_info_iter)?;
    let spl_token_program_info = next_account_info(account_info_iter)?;
    let system_program_info = next_account_info(account_info_iter)?;
    let _token_metadata_program_info = next_account_info(account_info_iter)?;

    // Check signers
    assert_signer(payer_info)?;
    assert_signer(authority_info)?;

    assert_owned_by(
        collection_mint_info,
        &spl_token::ID,
        MigrationError::IncorrectMintProgramOwner,
    )?;

    assert_owned_by(
        collection_metadata_info,
        &mpl_token_metadata::ID,
        MigrationError::IncorrectMetadataProgramOwner,
    )?;

    assert_owned_by(
        migration_state_info,
        program_id,
        MigrationError::IncorrectMigrationStateProgramOwner,
    )?;

    // Check program ids
    if spl_token_program_info.key != &SPL_TOKEN_ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    if system_program_info.key != &solana_program::system_program::ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    if _token_metadata_program_info.key != &mpl_token_metadata::ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Relationship validation

    metadata_derived_from_mint(collection_metadata_info, collection_mint_info)?;
    migration_state_derived_from_mint(migration_state_info, collection_mint_info)?;

    // Deserialize needed account states.
    let mut migration_state = MigrationState::from_account_info(migration_state_info)?;
    let collection_metadata = Metadata::from_account_info(collection_metadata_info)?;

    incoming_collection_mint_matches_stored(collection_mint_info, &migration_state)?;
    incoming_collection_authority_matches_stored(authority_info, &migration_state)?;
    // Update authority on collection metadata matches the authority stored in the migration state.
    update_authority_matches(
        &collection_metadata,
        &migration_state.collection_info.authority,
    )?;

    // The delegate record must match the correct derivation
    // with the mint from the migration state account and the
    // program signer as the delegate.
    assert_derivation(
        &mpl_token_metadata::ID,
        delegate_record_info,
        &[
            mpl_token_metadata::state::PREFIX.as_bytes(),
            mpl_token_metadata::ID.as_ref(),
            migration_state.collection_info.mint.as_ref(),
            mpl_token_metadata::pda::COLLECTION_AUTHORITY.as_bytes(),
            PROGRAM_SIGNER.as_ref(),
        ],
        MigrationError::InvalidDelegateRecordDerivation,
    )?;

    if !delegate_record_info.data_is_empty() {
        // Check that the authority matches for the cases where we don't create the record.
        let authority_record = CollectionAuthorityRecord::from_account_info(delegate_record_info)?;

        // If it doesn't match we need to revoke the old delegate and create a new one.
        // This is safe to do because we are still requiring the authority is a signer and matches
        // the authority stored in the migration state.
        if authority_record.update_authority != Some(*authority_info.key) {
            let instruction = mpl_token_metadata::instruction::revoke_collection_authority(
                mpl_token_metadata::ID,
                *delegate_record_info.key,
                PROGRAM_SIGNER,
                *authority_info.key,
                *collection_metadata_info.key,
                *collection_mint_info.key,
            );

            let account_infos = vec![
                delegate_record_info.clone(),
                authority_info.clone(),
                delegate_info.clone(),
                collection_metadata_info.clone(),
                collection_mint_info.clone(),
                spl_token_program_info.clone(),
                system_program_info.clone(),
            ];

            invoke_signed(&instruction, &account_infos, &[]).unwrap();
        }
    }

    // If the delegate record is unitialized, then we CPI into
    // the token metadata program to initialize it.
    if delegate_record_info.data_is_empty() {
        let instruction = mpl_token_metadata::instruction::approve_collection_authority(
            mpl_token_metadata::ID,
            *delegate_record_info.key,
            PROGRAM_SIGNER,
            *authority_info.key,
            *payer_info.key,
            *collection_metadata_info.key,
            *collection_mint_info.key,
        );
        let account_infos = vec![
            delegate_record_info.clone(),
            authority_info.clone(),
            payer_info.clone(),
            delegate_info.clone(),
            collection_metadata_info.clone(),
            collection_mint_info.clone(),
            spl_token_program_info.clone(),
            system_program_info.clone(),
        ];

        invoke_signed(&instruction, &account_infos, &[]).unwrap();
    }

    // Migration must be unlocked
    if migration_state.status.is_locked {
        return Err(MigrationError::MigrationLocked.into());
    }

    // Migration can be enabled, set to "in progress", as long as no items have been
    // migrated yet. This allows people to reset the delegate record if they
    // change their update authority.
    if migration_state.status.items_migrated > 0 {
        return Err(MigrationError::MigrationInProgress.into());
    }

    migration_state.collection_info.delegate_record = *delegate_record_info.key;
    migration_state.status.in_progress = true;
    migration_state.save(migration_state_info)?;

    Ok(())
}


