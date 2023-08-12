programs/nft-voter/src/tools/governance.rs
==========================================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: rs

    use anchor_lang::prelude::Pubkey;
use spl_governance::state::{token_owner_record, vote_record};

pub fn get_vote_record_address(
    program_id: &Pubkey,
    realm: &Pubkey,
    governing_token_mint: &Pubkey,
    governing_token_owner: &Pubkey,
    proposal: &Pubkey,
) -> Pubkey {
    let token_owner_record_key = token_owner_record::get_token_owner_record_address(
        program_id,
        realm,
        governing_token_mint,
        governing_token_owner,
    );

    vote_record::get_vote_record_address(program_id, proposal, &token_owner_record_key)
}


