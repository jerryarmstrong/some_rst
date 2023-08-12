cNft-Governance/governance-program-library/programs/cnft-voter/src/instructions/create_voter_weight_record.rs
=============================================================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    use crate::state::*;
use anchor_lang::prelude::*;
use anchor_spl::token::Mint;
use spl_governance::state::realm;

#[derive(Accounts)]
#[instruction(governing_token_owner: Pubkey)]
pub struct CreateVoterWeightRecord<'info> {
    #[account(
        init,
        seeds = [
            b"voter-weight-record".as_ref(),
            realm.key().as_ref(),
            realm_governing_token_mint.key().as_ref(),
            governing_token_owner.as_ref()
        ],
        bump,
        payer = payer,
        space = VoterWeightRecord::get_space(),
    )]
    pub voter_weight_record: Account<'info, VoterWeightRecord>,


    /// The program id of the spl-governance program the realm belongs to
    /// CHECK: Can be any instance of spl-governance and it's not known at the compilation time
    #[account(executable)]
    pub governance_program_id: UncheckedAccount<'info>,

    /// CHECK: Owned by spl-governance instance specified in governance_program_id
    #[account(owner = governance_program_id.key())]
    pub realm: UncheckedAccount<'info>,

    pub realm_governing_token_mint: Account<'info, Mint>, // should I name it governing_token_mint?

    #[account(mut)]
    payer: Signer<'info>,

    pub system_program: Program<'info, System>,
}

pub fn create_voter_weight_record(ctx: Context<CreateVoterWeightRecord>, governing_token_owner: Pubkey) -> Result<()> {
    let voter_weight_record = &mut ctx.accounts.voter_weight_record;

    let _realm = realm::get_realm_data_for_governing_token_mint(
        &ctx.accounts.governance_program_id.key(),
        &ctx.accounts.realm,
        &ctx.accounts.realm_governing_token_mint.key(),
    );

    voter_weight_record.realm = ctx.accounts.realm.key();
    voter_weight_record.governing_token_mint = ctx.accounts.realm_governing_token_mint.key();
    voter_weight_record.governing_token_owner = governing_token_owner;

    voter_weight_record.voter_weight_expiry = Some(0);

    Ok(())
}

