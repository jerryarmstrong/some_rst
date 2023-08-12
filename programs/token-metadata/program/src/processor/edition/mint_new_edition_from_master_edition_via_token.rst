programs/token-metadata/program/src/processor/edition/mint_new_edition_from_master_edition_via_token.rs
=======================================================================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    use solana_program::{account_info::AccountInfo, entrypoint::ProgramResult, pubkey::Pubkey};

use crate::{
    processor::all_account_infos,
    utils::{
        fee::{levy, set_fee_flag, LevyArgs},
        process_mint_new_edition_from_master_edition_via_token_logic,
        MintNewEditionFromMasterEditionViaTokenLogicArgs,
    },
};

pub fn process_mint_new_edition_from_master_edition_via_token<'a>(
    program_id: &'a Pubkey,
    accounts: &'a [AccountInfo<'a>],
    edition: u64,
) -> ProgramResult {
    all_account_infos!(
        accounts,
        new_metadata_account_info,
        new_edition_account_info,
        master_edition_account_info,
        mint_info,
        edition_marker_info,
        mint_authority_info,
        payer_account_info,
        owner_account_info,
        token_account_info,
        update_authority_info,
        master_metadata_account_info,
        token_program_account_info,
        system_account_info
    );

    // Levy fees first, to fund the metadata account with rent + fee amount.
    levy(LevyArgs {
        payer_account_info,
        token_metadata_pda_info: new_metadata_account_info,
    })?;

    process_mint_new_edition_from_master_edition_via_token_logic(
        program_id,
        MintNewEditionFromMasterEditionViaTokenLogicArgs {
            new_metadata_account_info,
            new_edition_account_info,
            master_edition_account_info,
            mint_info,
            edition_marker_info,
            mint_authority_info,
            payer_account_info,
            owner_account_info,
            token_account_info,
            update_authority_info,
            master_metadata_account_info,
            token_program_account_info,
            system_account_info,
        },
        edition,
    )?;

    // Set fee flag after metadata account is created.
    set_fee_flag(new_metadata_account_info)
}


