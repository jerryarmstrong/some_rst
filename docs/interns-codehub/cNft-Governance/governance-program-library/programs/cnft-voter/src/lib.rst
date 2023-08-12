cNft-Governance/governance-program-library/programs/cnft-voter/src/lib.rs
=========================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    #![allow(clippy::result_large_err)]
use anchor_lang::prelude::*;
pub mod error;
mod instructions;
use instructions::*;
pub mod state;
pub mod utils;
use crate::state::*;
pub use mpl_bubblegum::state::metaplex_adapter::MetadataArgs;

declare_id!("GcNftjiDYoAZpMRAQrYx51GJp7tEhSgMKqSfR4zeoCFV");

#[program]
pub mod cnft_voter {
    use super::*; //use to bring the CPI struct into the scope of the program
    use crate::state::{VoterWeightAction, CompressedNftAsset};
    // use mpl_bubblegum::state::metaplex_adapter::MetadataArgs;

    pub fn create_registrar(ctx: Context<CreateRegistrar>, max_collections: u8) -> Result<()> {
        log_version();
        instructions::create_registrar(ctx, max_collections)
    }

    pub fn create_voter_weight_record(
        ctx: Context<CreateVoterWeightRecord>,
        governing_token_owner: Pubkey,
    ) -> Result<()> {
        log_version();
        instructions::create_voter_weight_record(ctx, governing_token_owner)
    }

    pub fn create_max_voter_weight_record(ctx: Context<CreateMaxVoterWeightRecord>) -> Result<()> {
        log_version();
        instructions::create_max_voter_weight_record(ctx)
    }

    pub fn update_voter_weight_record<'a, 'b, 'c, 'info>(
        ctx: Context<'a, 'b, 'c, 'info, UpdateVoterWeightRecord<'info>>,
        voter_weight_action: VoterWeightAction,
        // cnft_info_len: u32,
        params: Vec<CompressedNftAsset>,
    ) -> Result<()> {
        log_version();
        instructions::update_voter_weight_record(ctx, voter_weight_action, &params)
    }

    pub fn configure_collection(
        ctx: Context<ConfigureCollection>,
        weight: u64,
        size: u32,
    ) -> Result<()> {
        log_version();
        instructions::configure_collection(ctx, weight, size)
    }

    pub fn cast_compressed_nft_vote<'a, 'b, 'c, 'info>(
        ctx: Context<'a, 'b, 'c, 'info, CastCompressedNftVote<'info>>,
        proposal: Pubkey,
        // cnft_info_len: u32,
        params: Vec<CompressedNftAsset>,
    ) -> Result<()> {
        log_version();
        instructions::cast_compressed_nft_vote(ctx, proposal, &params)
    }

    pub fn verify_compressed_nft_info<'a, 'b, 'c, 'info>(
        ctx: Context<'a, 'b, 'c, 'info, VerifyCompressedNftInfo<'info>>,
        params: CompressedNftAsset,
    ) -> Result<()> {
        log_version();
        instructions::verify_compressed_nft_info(ctx, &params)
    }

    pub fn relinquish_compressed_nft_vote(ctx: Context<RelinquishCompressedNftVote>) -> Result<()> {
        log_version();
        instructions::relinquish_compressed_nft_vote(ctx)
    }
}

fn log_version() {
    // TODO: Check if Anchor allows to log it before instruction is deserialized
    msg!("VERSION:{:?}", env!("CARGO_PKG_VERSION"));
}


