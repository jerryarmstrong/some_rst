cNft-Governance/governance-program-library/programs/cnft-voter/src/instructions/cast_cnft_vote.rs
=================================================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    use crate::error::CompressedNftVoterError;
use crate::{id, state::*};
use anchor_lang::prelude::*;
use anchor_lang::Accounts;
use spl_account_compression::program::SplAccountCompression;
use spl_governance_tools::account::create_and_serialize_account_signed;

#[derive(Accounts)]
#[instruction(proposal: Pubkey)]
pub struct CastCompressedNftVote<'info> {
    pub registrar: Account<'info, Registrar>,

    #[account(
        mut,
        constraint = voter_weight_record.realm == registrar.realm
        @ CompressedNftVoterError::InvalidVoterWeightRecordRealm,
        constraint = voter_weight_record.governing_token_mint == registrar.governing_token_mint
        @ CompressedNftVoterError::InvalidVoterWeightRecordMint,
    )]
    pub voter_weight_record: Account<'info, VoterWeightRecord>,

    // owner should be crate::id()
    /// CHECK: Owned by spl-governance instance specified in registrar.governance_program_id
    #[account(
        owner = registrar.governance_program_id
     )]
    voter_token_owner_record: UncheckedAccount<'info>,

    /// CHECK: unsafe
    pub merkle_tree: UncheckedAccount<'info>,
    /// CHECK: This account is checked in the instruction
    pub leaf_owner: UncheckedAccount<'info>,
    /// CHECK: This account is checked in the instruction
    pub leaf_delegate: UncheckedAccount<'info>,

    pub voter_authority: Signer<'info>,
    #[account(mut)]
    pub payer: Signer<'info>,

    pub compression_program: Program<'info, SplAccountCompression>,
    pub system_program: Program<'info, System>,
}

// so far only one nft is supported
pub fn cast_compressed_nft_vote<'a, 'b, 'c, 'info>(
    ctx: Context<'a, 'b, 'c, 'info, CastCompressedNftVote<'info>>,
    proposal: Pubkey,
    params: &Vec<CompressedNftAsset>,
) -> Result<()> {
    let registrar = &ctx.accounts.registrar;
    let voter_weight_record = &mut ctx.accounts.voter_weight_record;
    let merkle_tree = &ctx.accounts.merkle_tree.to_account_info();
    let leaf_owner = &ctx.accounts.leaf_owner.to_account_info();
    let leaf_delegate = &ctx.accounts.leaf_delegate.to_account_info();
    let remaining_accounts = &mut ctx.remaining_accounts.to_vec();
    let rent = Rent::get()?;
    let mut voter_weight = 0u64;
    let mut unique_asset_ids: Vec<Pubkey> = vec![];

    let governing_token_owner = resolve_governing_token_owner(
        registrar,
        &ctx.accounts.voter_token_owner_record,
        &ctx.accounts.voter_authority,
        voter_weight_record,
    )?;

    let mut start: usize = 0;
    for i in 0..params.len() {
        let param = &params[i];
        let proof_len = param.proof_len;
        let cnft_info =
            &remaining_accounts[start..(start + proof_len as usize + 1)];
        let proofs = cnft_info[0..proof_len as usize].to_vec();
        let cnft_vote_record_info = cnft_info[proof_len as usize].clone();
        let (cnft_vote_weight, asset_id) = resolve_cnft_vote_weight(
            &registrar,
            &governing_token_owner,
            &merkle_tree,
            &mut unique_asset_ids,
            &leaf_owner,
            &leaf_delegate,
            param,
            proofs,
            &ctx.accounts.compression_program.to_account_info(),
        )?;

        voter_weight = voter_weight.checked_add(cnft_vote_weight as u64).unwrap();
        let cnft_vote_record = CompressedNftVoteRecord {
            account_discriminator: CompressedNftVoteRecord::ACCOUNT_DISCRIMINATOR,
            proposal,
            asset_id,
            governing_token_owner,
            reserved: [0; 8],
        };
        require!(
            cnft_vote_record_info.data_is_empty(),
            CompressedNftVoterError::NftAlreadyVoted
        );
        create_and_serialize_account_signed(
            &ctx.accounts.payer.to_account_info(),
            &cnft_vote_record_info,
            &cnft_vote_record,
            &[b"cnft-vote-record", proposal.as_ref(), asset_id.as_ref()],
            &id(),
            &ctx.accounts.system_program.to_account_info(),
            &rent,
            0,
        )?;
        
        start += proof_len as usize + 1;
    }

    if voter_weight_record.weight_action_target == Some(proposal)
        && voter_weight_record.weight_action == Some(VoterWeightAction::CastVote)
    {
        // add up if there are more than one nft
        voter_weight_record.voter_weight = voter_weight_record
            .voter_weight
            .checked_add(voter_weight)
            .unwrap();
    } else {
        voter_weight_record.voter_weight = voter_weight;
    }

    voter_weight_record.voter_weight_expiry = Some(Clock::get()?.slot);

    // The record is only valid for casting vote on the given Proposal
    voter_weight_record.weight_action = Some(VoterWeightAction::CastVote);
    voter_weight_record.weight_action_target = Some(proposal);

    Ok(())
}


