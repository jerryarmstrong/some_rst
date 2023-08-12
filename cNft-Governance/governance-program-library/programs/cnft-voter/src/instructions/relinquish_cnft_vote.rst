cNft-Governance/governance-program-library/programs/cnft-voter/src/instructions/relinquish_cnft_vote.rs
=======================================================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;
use crate::state::*;
use crate::utils::governance::*;
use crate::error::CompressedNftVoterError;
use spl_governance::state::{governance, proposal, enums::ProposalState};
use spl_governance_tools::account::dispose_account;



/// Disposes NftVoteRecord and recovers the rent from the accounts
/// It can only be executed when voting on the target Proposal ended or voter withdrew vote from the Proposal
#[derive(Accounts)]
pub struct RelinquishCompressedNftVote<'info> {
    pub registrar: Account<'info, Registrar>,

    #[account(
        mut,
        constraint = voter_weight_record.realm == registrar.realm @ CompressedNftVoterError::InvalidVoterWeightRecordRealm,
        constraint = voter_weight_record.governing_token_mint == registrar.governing_token_mint @ CompressedNftVoterError::InvalidVoterWeightRecordMint,
    )]
    pub voter_weight_record: Account<'info, VoterWeightRecord>,

    /// CHECK: Owned by spl-governance instance specified in registrar.governance_program_id
    #[account(owner = registrar.governance_program_id)]
    pub governance: UncheckedAccount<'info>,

    /// CHECK: Owned by spl-governance instance specified in registrar.governance_program_id
    #[account(owner = registrar.governance_program_id)]
    pub proposal: UncheckedAccount<'info>,

    /// CHECK: Owned by spl-governance instance specified in registrar.governance_program_id
    #[account(owner = registrar.governance_program_id)]
    voter_token_owner_record: UncheckedAccount<'info>,

    pub voter_authority: Signer<'info>,

    /// CHECK: Owned by spl-governance instance specified in registrar.governance_program_id
    pub vote_record: UncheckedAccount<'info>,

    /// CHECK: The beneficiary who receives lamports from the disposed CompressedNftVoterRecord accounts can be any account
    #[account(mut)]
    pub beneficiary: UncheckedAccount<'info>,

}

pub fn relinquish_compressed_nft_vote(ctx: Context<RelinquishCompressedNftVote>) -> Result<()> {
    let registrar = &ctx.accounts.registrar;
    let voter_weight_record = &mut ctx.accounts.voter_weight_record;
    
    let governing_token_owner = resolve_governing_token_owner(
        registrar, 
        &ctx.accounts.voter_token_owner_record, 
        &ctx.accounts.voter_authority, 
        voter_weight_record
    )?;

    let _governance = governance::get_governance_data_for_realm(
        &registrar.governance_program_id,
        &ctx.accounts.governance,
        &registrar.realm,
    )?;

    let proposal = proposal::get_proposal_data_for_governance_and_governing_mint(
        &registrar.governance_program_id,
        &ctx.accounts.proposal,
        &ctx.accounts.governance.key(),
        &registrar.governing_token_mint,    
    )?;

    if proposal.state == ProposalState::Voting {
        let vote_record_info = &ctx.accounts.vote_record.to_account_info();

        let vote_record_key = get_vote_record_address(
            &registrar.governance_program_id,
            &registrar.realm,
            &registrar.governing_token_mint,
            &governing_token_owner,
            &ctx.accounts.proposal.key(),
        );

        require!(
            vote_record_key == vote_record_info.key(),
            CompressedNftVoterError::InvalidVoteRecordAccount
        );

        require!(
            // VoteRecord doesn't exist if data is empty or account_type is 0 when the account was disposed in the same Tx
            vote_record_info.data_is_empty() || vote_record_info.try_borrow_data().unwrap()[0] == 0,
            CompressedNftVoterError::VoteRecordMustBeWithdrawn
        );
    }

    // Prevent relinquishing NftVoteRecords within the VoterWeightRecord expiration period
    // It's needed when multiple stacked voter-weight plugins are used
    // Without the assertion the following vector of attack exists
    // 1) nft-voter.cast_nft_vote()
    // 2) voter-weight-plugin.cast_vote()
    // 3) nft-voter.relinquish_nft_vote()
    // 4) spl-gov.cast_vote() -> spl-gov uses VoterWeightRecord provided by voter-weight-plugin in step 2) while the nft vote is withdrawn and could be used to vote again
    if voter_weight_record.voter_weight_expiry >= Some(Clock::get()?.slot) {
        return err!(CompressedNftVoterError::VoterWeightRecordMustBeExpired);
    }

    // Dispose all NftVoteRecords
    for cnft_vote_record_info in ctx.remaining_accounts.iter() {
        // Ensure NftVoteRecord is for the given Proposal and TokenOwner
        let _cnft_vote_record = get_cnft_vote_record_data_for_proposal_and_token_owner(
            cnft_vote_record_info,
            &ctx.accounts.proposal.key(),
            &governing_token_owner,
        )?;

        dispose_account(cnft_vote_record_info, &ctx.accounts.beneficiary)?;
    }

    // Reset VoterWeightRecord and set expiry to expired to prevent it from being used
    voter_weight_record.voter_weight = 0;
    voter_weight_record.voter_weight_expiry = Some(0);

    voter_weight_record.weight_action_target = None;


    Ok(())
}

