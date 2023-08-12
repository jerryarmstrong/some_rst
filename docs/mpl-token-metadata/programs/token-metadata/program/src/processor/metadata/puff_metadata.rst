programs/token-metadata/program/src/processor/metadata/puff_metadata.rs
=======================================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    use solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, pubkey::Pubkey};

use crate::{
    assertions::assert_owned_by,
    processor::all_account_infos,
    state::{Metadata, TokenMetadataAccount, EDITION, PREFIX},
    utils::puff_out_data_fields,
};

/// Puff out the variable length fields to a fixed length on a metadata
/// account in a permissionless way.
pub fn process_puff_metadata_account(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    all_account_infos!(accounts, metadata_account_info);

    let mut metadata = Metadata::from_account_info(metadata_account_info)?;

    assert_owned_by(metadata_account_info, program_id)?;

    puff_out_data_fields(&mut metadata);

    let edition_seeds = &[
        PREFIX.as_bytes(),
        program_id.as_ref(),
        metadata.mint.as_ref(),
        EDITION.as_bytes(),
    ];
    let (_, edition_bump_seed) = Pubkey::find_program_address(edition_seeds, program_id);
    metadata.edition_nonce = Some(edition_bump_seed);

    metadata.save(&mut metadata_account_info.try_borrow_mut_data()?)?;
    Ok(())
}


