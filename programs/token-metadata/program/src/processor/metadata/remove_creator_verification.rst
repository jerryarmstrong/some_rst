programs/token-metadata/program/src/processor/metadata/remove_creator_verification.rs
=====================================================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    use mpl_utils::assert_signer;
use solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, pubkey::Pubkey};

use crate::{
    assertions::assert_owned_by,
    error::MetadataError,
    processor::all_account_infos,
    state::{Metadata, TokenMetadataAccount},
};

pub fn process_remove_creator_verification(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    all_account_infos!(accounts, metadata_info, creator_info);

    assert_signer(creator_info)?;
    assert_owned_by(metadata_info, program_id)?;

    let mut metadata = Metadata::from_account_info(metadata_info)?;

    if let Some(creators) = &mut metadata.data.creators {
        let mut found = false;
        for creator in creators {
            if creator.address == *creator_info.key {
                creator.verified = false;
                found = true;
                break;
            }
        }
        if !found {
            return Err(MetadataError::CreatorNotFound.into());
        }
    } else {
        return Err(MetadataError::NoCreatorsPresentOnMetadata.into());
    }
    metadata.save(&mut metadata_info.try_borrow_mut_data()?)?;

    Ok(())
}


