programs/token-metadata/program/src/processor/metadata/update_primary_sale_happened_via_token.rs
================================================================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    use solana_program::{
    account_info::AccountInfo, entrypoint::ProgramResult, program_error::ProgramError,
    pubkey::Pubkey,
};
use spl_token::state::Account;

use crate::{
    assertions::{assert_initialized, assert_owned_by},
    error::MetadataError,
    processor::all_account_infos,
    state::{Metadata, TokenMetadataAccount},
};

pub fn process_update_primary_sale_happened_via_token(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    all_account_infos!(
        accounts,
        metadata_account_info,
        owner_info,
        token_account_info
    );

    let token_account: Account = assert_initialized(token_account_info)?;
    let mut metadata = Metadata::from_account_info(metadata_account_info)?;

    assert_owned_by(metadata_account_info, program_id)?;
    assert_owned_by(token_account_info, &spl_token::ID)?;

    if !owner_info.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    if token_account.owner != *owner_info.key {
        return Err(MetadataError::OwnerMismatch.into());
    }

    if token_account.amount == 0 {
        return Err(MetadataError::NoBalanceInAccountForAuthorization.into());
    }

    if token_account.mint != metadata.mint {
        return Err(MetadataError::MintMismatch.into());
    }

    metadata.primary_sale_happened = true;
    metadata.save(&mut metadata_account_info.try_borrow_mut_data()?)?;

    Ok(())
}


