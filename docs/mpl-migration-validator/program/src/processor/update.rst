program/src/processor/update.rs
===============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use super::*;

pub fn update_state(
    _program_id: &Pubkey,
    accounts: &[AccountInfo],
    args: UpdateArgs,
) -> ProgramResult {
    let UpdateArgs {
        rule_set,
        collection_size,
        new_update_authority,
    } = args;

    // Fetch accounts
    let account_info_iter = &mut accounts.iter();
    let authority_info = next_account_info(account_info_iter)?;
    let migration_state_info = next_account_info(account_info_iter)?;

    // Validate Accounts
    assert_signer(authority_info)?;

    assert_owned_by(
        migration_state_info,
        &crate::ID,
        MigrationError::IncorrectMigrationStateProgramOwner,
    )?;

    // Deserialize the migration state
    let mut migration_state = MigrationState::from_account_info(migration_state_info)?;

    // Ensure the authority matches
    incoming_collection_authority_matches_stored(authority_info, &migration_state)?;

    // If given a collection_size, update the state.
    if let Some(collection_size) = collection_size {
        migration_state.collection_info.size = collection_size;
    }

    // Only allow updating rule set or update authority if no items have been migrated yet.

    if let Some(rule_set) = rule_set {
        if migration_state.status.items_migrated > 0 {
            return Err(MigrationError::MigrationInProgress.into());
        }
        migration_state.collection_info.rule_set = rule_set;
    }

    if let Some(new_update_authority) = new_update_authority {
        if migration_state.status.items_migrated > 0 {
            return Err(MigrationError::MigrationInProgress.into());
        }
        migration_state.collection_info.authority = new_update_authority;
    }

    // Perform a time check to check eligibility for migration
    let now = Clock::get()?.unix_timestamp;
    let wait_period_over = now >= migration_state.status.unlock_time;

    if migration_state.unlock_method == UnlockMethod::Timed
        && wait_period_over
        && migration_state.status.is_locked
    {
        migration_state.status.is_locked = false;
    }

    // write updated state if there was a change
    migration_state.save(migration_state_info)?;

    Ok(())
}


