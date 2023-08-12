program/src/processor/migrate/processor.rs
==========================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use solana_program::program_pack::Pack;
use spl_token::state::Mint;

use crate::errors::MigrationError;

use super::*;

pub fn migrate_item<'a>(program_id: &'a Pubkey, accounts: &'a [AccountInfo<'a>]) -> ProgramResult {
    // Fetch accounts
    let account_info_iter = &mut accounts.iter();
    let metadata_info = next_account_info(account_info_iter)?;
    let edition_info = next_account_info(account_info_iter)?;
    let token_info = next_account_info(account_info_iter)?;
    let token_owner_info = next_account_info(account_info_iter)?;
    let token_owner_program_info = next_account_info(account_info_iter)?;
    let token_owner_program_buffer_info = next_account_info(account_info_iter)?;
    let mint_info = next_account_info(account_info_iter)?;
    let payer_info = next_account_info(account_info_iter)?;
    let program_signer_info = next_account_info(account_info_iter)?;
    let collection_metadata_info = next_account_info(account_info_iter)?;
    let delegate_record_info = next_account_info(account_info_iter)?;
    let token_record_info = next_account_info(account_info_iter)?;
    let system_program_info = next_account_info(account_info_iter)?;
    let sysvar_instructions_info = next_account_info(account_info_iter)?;
    let spl_token_program_info = next_account_info(account_info_iter)?;
    let mpl_token_auth_rules_program_info = next_account_info(account_info_iter)?;
    let auth_rule_set_info = next_account_info(account_info_iter)?;
    let migration_state_info = next_account_info(account_info_iter)?;
    let token_metadata_program_info = next_account_info(account_info_iter)?;

    let ctx = AccountContext {
        program_id,
        payer_info,
        metadata_info,
        edition_info,
        mint_info,
        token_owner_info,
        token_owner_program_info,
        token_owner_program_buffer_info,
        delegate_record_info,
        migration_state_info,
        program_signer_info,
        auth_rule_set_info,
        system_program_info,
        sysvar_instructions_info,
        spl_token_program_info,
        token_metadata_program_info,
    };

    // Validate Accounts
    validate_accounts(&ctx)?;

    // Deserialize accounts
    let metadata = Metadata::from_account_info(ctx.metadata_info)
        .map_err(|_| MigrationError::InvalidMetadata)?;

    let collection_metadata = Metadata::from_account_info(collection_metadata_info)
        .map_err(|_| MigrationError::InvalidMetadata)?;

    let mut migration_state = MigrationState::from_account_info(ctx.migration_state_info)?;

    let mint = Mint::unpack(&ctx.mint_info.data.borrow())?;
    let token = Account::unpack(&token_info.data.borrow())?;

    let program_signer = ProgramSigner::from_account_info(ctx.program_signer_info)?;
    let signers_seeds: &[&[u8]] = &[b"signer", &[program_signer.bump]];

    let data_context = DataContext {
        metadata: &metadata,
        collection_metadata: &collection_metadata,
        migration_state: &migration_state,
        mint: &mint,
        token: &token,
    };

    // Validate relatonships between accounts
    validate_relationships(&ctx, &data_context)?;

    // Validate the delegate record is correct.
    validate_delegate(&ctx, &data_context)?;

    // Validate this item passes all eligibility rules.
    validate_eligibility(&ctx, &data_context)?;

    // Migrate the item by CPI'ing into Token Metadata.
    let args = MigrateArgs::V1 {
        migration_type: MigrationType::ProgrammableV1,
        rule_set: if migration_state.collection_info.rule_set == Pubkey::default() {
            None
        } else {
            Some(migration_state.collection_info.rule_set)
        },
    };

    let account_infos = vec![
        metadata_info.clone(),
        edition_info.clone(),
        token_info.clone(),
        token_owner_info.clone(),
        mint_info.clone(),
        payer_info.clone(),
        program_signer_info.clone(),
        collection_metadata_info.clone(),
        delegate_record_info.clone(),
        token_record_info.clone(),
        system_program_info.clone(),
        sysvar_instructions_info.clone(),
        spl_token_program_info.clone(),
        mpl_token_auth_rules_program_info.clone(),
        auth_rule_set_info.clone(),
    ];

    let mut builder = MigrateBuilder::new();
    let migrate = builder
        .metadata(*metadata_info.key)
        .edition(*edition_info.key)
        .token(*token_info.key)
        .token_owner(*token_owner_info.key)
        .mint(*mint_info.key)
        .payer(*payer_info.key)
        .authority(*program_signer_info.key)
        .collection_metadata(*collection_metadata_info.key)
        .delegate_record(*delegate_record_info.key)
        .token_record(*token_record_info.key)
        .build(args)
        .map_err(|_| MigrationError::InvalidInstruction)?;

    let instruction = migrate.instruction();

    invoke_signed(&instruction, &account_infos, &[signers_seeds]).unwrap();

    // Increment the number of items migrated
    migration_state.status.items_migrated = migration_state
        .status
        .items_migrated
        .checked_add(1)
        .ok_or(MigrationError::Overflow)?;

    // Serialize the migration state
    migration_state.save(migration_state_info)?;

    Ok(())
}


