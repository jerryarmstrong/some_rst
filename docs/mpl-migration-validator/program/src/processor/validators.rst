program/src/processor/validators.rs
===================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use super::*;

pub(crate) fn metadata_belongs_to_mint(
    metadata: &Metadata,
    mint: &Pubkey,
) -> Result<(), ProgramError> {
    if metadata.mint != *mint {
        return Err(MigrationError::MetadataMintMistmatch.into());
    }
    Ok(())
}

pub(crate) fn update_authority_matches(
    metadata: &Metadata,
    authority: &Pubkey,
) -> Result<(), ProgramError> {
    if metadata.update_authority != *authority {
        return Err(MigrationError::InvalidAuthority.into());
    }
    Ok(())
}

pub(crate) fn verified_collection_member(
    item_metadata: &Metadata,
    collection_mint_pubkey: &Pubkey,
) -> Result<(), ProgramError> {
    if item_metadata.collection.is_none() {
        return Err(MigrationError::CollectionNotFound.into());
    }

    let collection = item_metadata.collection.as_ref().unwrap();

    if !collection.verified || collection.key != *collection_mint_pubkey {
        return Err(MigrationError::NotCollectionMember.into());
    }
    Ok(())
}

pub(crate) fn metadata_derived_from_mint(
    metadata_info: &AccountInfo,
    mint_info: &AccountInfo,
) -> Result<(), ProgramError> {
    assert_derivation(
        &mpl_token_metadata::ID,
        metadata_info,
        &[
            PREFIX.as_bytes(),
            mpl_token_metadata::ID.as_ref(),
            mint_info.key.as_ref(),
        ],
        MigrationError::MetadataMintMistmatch,
    )?;
    Ok(())
}

pub(crate) fn edition_derived_from_mint(
    edition_info: &AccountInfo,
    mint_info: &AccountInfo,
) -> Result<(), ProgramError> {
    assert_derivation(
        &mpl_token_metadata::ID,
        edition_info,
        &[
            PREFIX.as_bytes(),
            mpl_token_metadata::ID.as_ref(),
            mint_info.key.as_ref(),
            EDITION.as_bytes(),
        ],
        MigrationError::InvalidEditionDerivation,
    )?;
    Ok(())
}

pub(crate) fn migration_state_derived_from_mint(
    migration_state_info: &AccountInfo,
    mint_info: &AccountInfo,
) -> Result<(), ProgramError> {
    assert_derivation(
        &crate::ID,
        migration_state_info,
        &[b"migration", mint_info.key.as_ref()],
        MigrationError::InvalidMigrationStateDerivation,
    )?;
    Ok(())
}

pub(crate) fn token_belongs_to_mint(
    token: &TokenAccount,
    mint_pubkey: &Pubkey,
) -> Result<(), ProgramError> {
    if token.mint != *mint_pubkey {
        return Err(MigrationError::TokenMintMismatch.into());
    }
    Ok(())
}

pub(crate) fn incoming_collection_mint_matches_stored(
    collection_mint_info: &AccountInfo,
    migration_state: &MigrationState,
) -> Result<(), ProgramError> {
    if migration_state.collection_info.mint != *collection_mint_info.key {
        return Err(MigrationError::CollectionMintMismatch.into());
    }
    Ok(())
}

pub(crate) fn incoming_collection_authority_matches_stored(
    collection_authority_info: &AccountInfo,
    migration_state: &MigrationState,
) -> Result<(), ProgramError> {
    if migration_state.collection_info.authority != *collection_authority_info.key {
        return Err(MigrationError::InvalidAuthority.into());
    }
    Ok(())
}

pub(crate) fn incoming_auth_rules_matches_stored(
    auth_rules_info: &AccountInfo,
    migration_state: &MigrationState,
) -> Result<(), ProgramError> {
    if migration_state.collection_info.rule_set != *auth_rules_info.key {
        return Err(MigrationError::InvalidRuleSet.into());
    }
    Ok(())
}

pub(crate) fn token_owned_by(token: &TokenAccount, owner: &Pubkey) -> Result<(), ProgramError> {
    if token.owner != *owner {
        return Err(MigrationError::TokenOwnerMismatch.into());
    }
    Ok(())
}


