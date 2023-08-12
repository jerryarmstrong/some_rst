program/src/processor/initialize.rs
===================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    // use mpl_token_metadata::state::TokenStandard;

// use crate::state::{CollectionInfo, MigrationStatus};

// use super::*;

// pub fn initialize_migration(
//     program_id: &Pubkey,
//     accounts: &[AccountInfo],
//     args: InitializeArgs,
// ) -> ProgramResult {
//     let InitializeArgs {
//         rule_set,
//         unlock_method,
//         collection_size,
//     } = args;

//     // Fetch accounts
//     let account_info_iter = &mut accounts.iter();
//     let payer_info = next_account_info(account_info_iter)?;
//     let authority_info = next_account_info(account_info_iter)?;
//     let collection_mint_info = next_account_info(account_info_iter)?;
//     let collection_metadata_info = next_account_info(account_info_iter)?;
//     let migration_state_info = next_account_info(account_info_iter)?;
//     let system_program_info = next_account_info(account_info_iter)?;

//     // Validate Accounts

//     // Both accounts must be signers, but can be the same account
//     // if collection authority is paying.
//     assert_signer(payer_info)?;
//     assert_signer(authority_info)?;

//     if system_program_info.key != &solana_program::system_program::ID {
//         return Err(ProgramError::IncorrectProgramId);
//     }

//     // Ensure that these accounts all belong together
//     // * Metadata must be derived from the mint address
//     // * Authority must be the update_authority on the metadata struct

//     // Properly derived Metadata account
//     assert_derivation(
//         &mpl_token_metadata::ID,
//         collection_metadata_info,
//         &[
//             b"metadata",
//             mpl_token_metadata::ID.as_ref(),
//             collection_mint_info.key.as_ref(),
//         ],
//         MigrationError::MetadataMintMistmatch,
//     )?;

//     // This ensures the account isn't empty as the deserialization fails if the account doesn't have the correct size.
//     // It also checks that the account is actually owned by the Token Metadata program.
//     let collection_metadata = Metadata::from_account_info(collection_metadata_info)
//         .map_err(|_| MigrationError::InvalidMetadata)?;

//     // Ensure that the authority is the update authority on the metadata
//     if collection_metadata.update_authority != *authority_info.key {
//         return Err(MigrationError::InvalidAuthority.into());
//     }

//     // For good measure we check that the mint is the mint on the metadata.
//     if collection_metadata.mint != *collection_mint_info.key {
//         return Err(MigrationError::MetadataMintMistmatch.into());
//     }

//     // The Collection NFT should be a NonFungible type, meaning it has a Master Edition.
//     if let Some(token_standard) = collection_metadata.token_standard {
//         if token_standard != TokenStandard::NonFungible {
//             return Err(MigrationError::InvalidTokenStandard.into());
//         }
//     } else {
//         // No token standard set.
//         return Err(MigrationError::MissingTokenStandard.into());
//     }

//     // The migrate state account must must match the correct derivation
//     let bump = assert_derivation(
//         program_id,
//         migration_state_info,
//         &[b"migration", collection_mint_info.key.as_ref()],
//         MigrationError::InvalidMigrationStateDerivation,
//     )?;
//     let state_seeds = &[b"migration", collection_mint_info.key.as_ref(), &[bump]];

//     if system_program_info.key != &solana_program::system_program::ID {
//         return Err(ProgramError::IncorrectProgramId);
//     }

//     let unlock_time = Clock::get()?.unix_timestamp + MIGRATION_WAIT_PERIOD;

//     let collection_info = CollectionInfo {
//         authority: *authority_info.key,
//         mint: *collection_mint_info.key,
//         delegate_record: Pubkey::default(),
//         rule_set: rule_set.unwrap_or_default(),
//         size: collection_size,
//     };

//     let status = MigrationStatus {
//         unlock_time,
//         is_locked: true,
//         in_progress: false,
//         items_migrated: 0,
//     };

//     let migration_state = MigrationState {
//         collection_info,
//         unlock_method,
//         status,
//     };

//     let serialized_data = migration_state.try_to_vec()?;
//     let data_len = serialized_data.len();

//     mpl_utils::create_or_allocate_account_raw(
//         *program_id,
//         migration_state_info,
//         system_program_info,
//         payer_info,
//         data_len,
//         state_seeds,
//     )?;

//     sol_memcpy(
//         &mut migration_state_info.data.borrow_mut(),
//         serialized_data.as_slice(),
//         data_len,
//     );

//     Ok(())
// }


