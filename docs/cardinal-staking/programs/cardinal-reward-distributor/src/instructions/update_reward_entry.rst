programs/cardinal-reward-distributor/src/instructions/update_reward_entry.rs
============================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct UpdateRewardEntryIx {
    pub multiplier: u64,
}

#[derive(Accounts)]
#[instruction(ix: UpdateRewardEntryIx)]
pub struct UpdateRewardEntryCtx<'info> {
    #[account(mut, constraint = reward_entry.reward_distributor == reward_distributor.key() @ ErrorCode::InvalidRewardDistributor)]
    reward_entry: Box<Account<'info, RewardEntry>>,
    reward_distributor: Box<Account<'info, RewardDistributor>>,
    #[account(constraint = authority.key() == reward_distributor.authority @ ErrorCode::InvalidRewardDistributorAuthority)]
    authority: Signer<'info>,
}

pub fn handler(ctx: Context<UpdateRewardEntryCtx>, ix: UpdateRewardEntryIx) -> Result<()> {
    let reward_entry = &mut ctx.accounts.reward_entry;
    reward_entry.multiplier = ix.multiplier;
    Ok(())
}


