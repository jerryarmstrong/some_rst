program/src/processor/close.rs
==============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use crate::utils::close_program_account;

use super::*;

pub fn close_migration_state(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Fetch accounts
    let account_info_iter = &mut accounts.iter();
    let authority_info = next_account_info(account_info_iter)?;
    let migration_state_info = next_account_info(account_info_iter)?;
    let system_program_info = next_account_info(account_info_iter)?;

    // Validate Accounts
    assert_signer(authority_info)?;

    if system_program_info.key != &solana_program::system_program::ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Paranoia.
    assert_owned_by(
        migration_state_info,
        program_id,
        MigrationError::IncorrectMigrationStateProgramOwner,
    )?;

    // Deserialize the migration state
    let migration_state = MigrationState::from_account_info(migration_state_info)?;

    assert_derivation(
        program_id,
        migration_state_info,
        &[b"migration", migration_state.collection_info.mint.as_ref()],
        MigrationError::InvalidMigrationStateDerivation,
    )?;

    // Ensure the authority matches
    incoming_collection_authority_matches_stored(authority_info, &migration_state)?;

    // Ensure the migration isn't in progress
    if migration_state.status.in_progress {
        return Err(MigrationError::MigrationInProgress.into());
    }

    // Do not allow closing after the migration is complete.
    if migration_state.status.items_migrated > 0 {
        return Err(MigrationError::MigrationAlreadyCompleted.into());
    }

    close_program_account(migration_state_info, authority_info)?;

    Ok(())
}


