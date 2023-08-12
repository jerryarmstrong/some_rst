program/src/processor/migrate/validate.rs
=========================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use mpl_token_metadata::{state::TokenStandard, utils::is_master_edition};
use mpl_utils::token::{get_mint_decimals, get_mint_supply};
use solana_program::bpf_loader_upgradeable::UpgradeableLoaderState;

use crate::utils::assert_valid_delegate;

use super::*;

pub(crate) fn validate_accounts(ctx: &AccountContext) -> Result<(), ProgramError> {
    // Signers
    assert_signer(ctx.payer_info)?;

    // Program ownership
    assert_owned_by(
        ctx.delegate_record_info,
        &mpl_token_metadata::ID,
        MigrationError::IncorrectDelegateRecordProgramOwner,
    )?;

    assert_owned_by(
        ctx.mint_info,
        &SPL_TOKEN_ID,
        MigrationError::IncorrectMintProgramOwner,
    )?;
    assert_owned_by(
        ctx.metadata_info,
        &mpl_token_metadata::ID,
        MigrationError::IncorrectMetadataProgramOwner,
    )?;
    assert_owned_by(
        ctx.migration_state_info,
        ctx.program_id,
        MigrationError::IncorrectMigrationStateProgramOwner,
    )?;

    // Programs
    if ctx.token_metadata_program_info.key != &mpl_token_metadata::ID {
        return Err(ProgramError::IncorrectProgramId);
    }
    if ctx.system_program_info.key != &solana_program::system_program::ID {
        return Err(ProgramError::IncorrectProgramId);
    }
    if ctx.spl_token_program_info.key != &SPL_TOKEN_ID {
        return Err(ProgramError::IncorrectProgramId);
    }
    if ctx.sysvar_instructions_info.key != &sysvar::instructions::ID {
        return Err(ProgramError::IncorrectProgramId);
    }

    Ok(())
}

pub(crate) fn validate_relationships(
    ctx: &AccountContext,
    data: &DataContext,
) -> Result<(), ProgramError> {
    // User provided
    let item_metadata = &data.metadata;
    let collection_metadata = &data.collection_metadata;
    let mint_pubkey = ctx.mint_info.key;
    let collection_mint_pubkey = &collection_metadata.mint;

    // Migration State
    let stored_collection_mint_pubkey = &data.migration_state.collection_info.mint;
    let stored_collection_authority_pubkey = &data.migration_state.collection_info.authority;

    // Collection NFT
    // The provided collection metadata must match the collection mint and update authority
    // stored on the migration state.
    metadata_belongs_to_mint(collection_metadata, stored_collection_mint_pubkey)?;
    update_authority_matches(collection_metadata, stored_collection_authority_pubkey)?;

    // Migration Item
    // The item's metadata and mint must match.
    metadata_belongs_to_mint(item_metadata, mint_pubkey)?;

    // The item's update authority must match that of the collection.
    update_authority_matches(item_metadata, stored_collection_authority_pubkey)?;

    // The item must actually be a verified member of the collection or must
    // be the collection NFT itself.
    if &item_metadata.mint != collection_mint_pubkey {
        verified_collection_member(item_metadata, collection_mint_pubkey)?;
    }

    // The passed in auth_rules account must match the one on the migration state.
    incoming_auth_rules_matches_stored(ctx.auth_rule_set_info, data.migration_state)?;

    // The item's edition must be derived from the item's mint.
    edition_derived_from_mint(ctx.edition_info, ctx.mint_info)?;

    // The item's edition must be a master edition.
    let mint_decimals = get_mint_decimals(ctx.mint_info)?;
    let mint_supply = get_mint_supply(ctx.mint_info)?;
    is_master_edition(ctx.edition_info, mint_decimals, mint_supply);

    // The token must belong to the mint
    token_belongs_to_mint(data.token, mint_pubkey)?;

    // The token must be owned by the specified owner
    token_owned_by(data.token, ctx.token_owner_info.key)?;

    // Token owner must be owned by the specified program
    assert_owned_by(
        ctx.token_owner_info,
        ctx.token_owner_program_info.key,
        MigrationError::IncorrectTokenOwnerProgramOwner,
    )?;

    // The token owner program buffer must be the correct one.
    // We only check upgradeble loader programs as we don't want to skip
    // anything owned by e.g. the SystemProgram.
    let state_opt: Option<UpgradeableLoaderState> =
        bincode::deserialize(&ctx.token_owner_program_info.data.borrow()).ok();

    if let Some(state) = state_opt {
        match state {
            UpgradeableLoaderState::Program {
                programdata_address,
            } => {
                if programdata_address != *ctx.token_owner_program_buffer_info.key {
                    return Err(MigrationError::IncorrectTokenOwnerProgramBuffer.into());
                }
            }
            _ => return Err(MigrationError::IncorrectTokenOwnerProgramOwner.into()),
        }
    }

    Ok(())
}

pub(crate) fn validate_eligibility(
    ctx: &AccountContext,
    data: &DataContext,
) -> Result<(), ProgramError> {
    // The Token Metadata edition PDA must have the freeze authority on the item.
    if data.mint.freeze_authority != COption::Some(*ctx.edition_info.key) {
        return Err(MigrationError::IncorrectFreezeAuthority.into());
    }

    // The item metadata must be mutable.
    if !data.metadata.is_mutable {
        return Err(MigrationError::ImmutableMetadata.into());
    }

    if let Some(token_standard) = data.metadata.token_standard {
        if token_standard != TokenStandard::NonFungible {
            return Err(MigrationError::IncorrectTokenStandard.into());
        }
    } else {
        let mint_decimals = get_mint_decimals(ctx.mint_info)?;
        let mint_supply = get_mint_supply(ctx.mint_info)?;

        if !is_master_edition(ctx.edition_info, mint_decimals, mint_supply) {
            return Err(MigrationError::IncorrectTokenStandard.into());
        }
    }

    // token owner program buffer defaults to crate ID if not provided,
    // so skip this check if that's the case.
    if ctx.token_owner_program_buffer_info.key != &crate::ID {
        // Do not migrate items owned by immutable programs.
        let state: UpgradeableLoaderState =
            bincode::deserialize(&ctx.token_owner_program_buffer_info.data.borrow())
                .map_err(|_| MigrationError::IncorrectTokenOwnerProgramBuffer)?;

        match state {
            UpgradeableLoaderState::ProgramData {
                slot: _,
                upgrade_authority_address,
            } => {
                if upgrade_authority_address.is_none() {
                    return Err(MigrationError::ImmutableProgramOwner.into());
                }
            }
            // If this isn't a ProgramData variant something is wrong.
            _ => return Err(MigrationError::IncorrectTokenOwnerProgramBuffer.into()),
        }
    }

    Ok(())
}

pub(crate) fn validate_delegate(
    ctx: &AccountContext,
    data: &DataContext,
) -> Result<(), ProgramError> {
    // Validate that the delegate is the program signer for the correct
    // mint and update authority.
    assert_valid_delegate(
        ctx.program_signer_info.key,
        ctx.delegate_record_info,
        data.collection_metadata,
        data.migration_state,
    )?;

    Ok(())
}


