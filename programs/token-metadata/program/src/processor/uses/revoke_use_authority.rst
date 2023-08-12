programs/token-metadata/program/src/processor/uses/revoke_use_authority.rs
==========================================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    use mpl_utils::assert_signer;
use solana_program::{
    account_info::AccountInfo, entrypoint::ProgramResult, program::invoke, pubkey::Pubkey,
};
use spl_token::instruction::revoke;

use crate::{
    assertions::{
        assert_owned_by,
        metadata::assert_currently_holding,
        uses::{
            assert_use_authority_derivation, assert_valid_bump, process_use_authority_validation,
        },
    },
    error::MetadataError,
    processor::all_account_infos,
    state::{Key, Metadata, TokenMetadataAccount, UseAuthorityRecord, UseMethod},
    utils::close_program_account,
};

pub fn process_revoke_use_authority(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    all_account_infos!(
        accounts,
        use_authority_record_info,
        owner_info,
        user_info,
        token_account_info,
        mint_info,
        metadata_info,
        token_program_account_info
    );

    let metadata = Metadata::from_account_info(metadata_info)?;
    if metadata.uses.is_none() {
        return Err(MetadataError::Unusable.into());
    }
    if *token_program_account_info.key != spl_token::ID {
        return Err(MetadataError::InvalidTokenProgram.into());
    }
    assert_signer(owner_info)?;
    assert_currently_holding(
        program_id,
        owner_info,
        metadata_info,
        &metadata,
        mint_info,
        token_account_info,
    )?;
    let data = use_authority_record_info.try_borrow_mut_data()?;
    process_use_authority_validation(data.len(), false)?;
    assert_owned_by(use_authority_record_info, program_id)?;
    let canonical_bump = assert_use_authority_derivation(
        program_id,
        use_authority_record_info,
        user_info,
        mint_info,
    )?;
    let mut record = UseAuthorityRecord::from_bytes(&data)?;
    if record.bump_empty() {
        record.bump = canonical_bump;
    }
    assert_valid_bump(canonical_bump, &record)?;
    let metadata_uses = metadata.uses.unwrap();
    if metadata_uses.use_method == UseMethod::Burn {
        invoke(
            &revoke(
                token_program_account_info.key,
                token_account_info.key,
                owner_info.key,
                &[],
            )
            .unwrap(),
            &[
                token_program_account_info.clone(),
                token_account_info.clone(),
                owner_info.clone(),
            ],
        )?;
    }

    // Drop use_authority_record_info account data borrow.
    drop(data);

    close_program_account(
        use_authority_record_info,
        owner_info,
        Key::UseAuthorityRecord,
    )
}


