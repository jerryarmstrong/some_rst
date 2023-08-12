programs/cardinal-reward-distributor/src/instructions/close_reward_entry.rs
===========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct CloseRewardEntryCtx<'info> {
    reward_distributor: Box<Account<'info, RewardDistributor>>,
    #[account(mut, close = authority, constraint = reward_entry.reward_distributor == reward_distributor.key() @ ErrorCode::InvalidRewardDistributor)]
    reward_entry: Box<Account<'info, RewardEntry>>,
    #[account(mut, constraint = reward_distributor.authority == authority.key() @ ErrorCode::InvalidAuthority)]
    authority: Signer<'info>,
}

pub fn handler(_ctx: Context<CloseRewardEntryCtx>) -> Result<()> {
    Ok(())
}


