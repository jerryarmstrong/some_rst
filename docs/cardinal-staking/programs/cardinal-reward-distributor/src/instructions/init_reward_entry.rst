programs/cardinal-reward-distributor/src/instructions/init_reward_entry.rs
==========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use cardinal_stake_pool::state::StakeEntry;

use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct InitRewardEntryCtx<'info> {
    #[account(
        init,
        payer = payer,
        space = REWARD_ENTRY_SIZE,
        seeds = [REWARD_ENTRY_SEED.as_bytes(), reward_distributor.key().as_ref(), stake_entry.key().as_ref()],
        bump,
    )]
    reward_entry: Box<Account<'info, RewardEntry>>,
    #[account(constraint = reward_distributor.stake_pool == stake_entry.pool)]
    stake_entry: Box<Account<'info, StakeEntry>>,
    #[account(mut)]
    reward_distributor: Box<Account<'info, RewardDistributor>>,
    #[account(mut)]
    payer: Signer<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<InitRewardEntryCtx>) -> Result<()> {
    let reward_distributor = &mut ctx.accounts.reward_distributor;
    let reward_entry = &mut ctx.accounts.reward_entry;
    reward_entry.bump = *ctx.bumps.get("reward_entry").unwrap();
    reward_entry.reward_distributor = reward_distributor.key();
    reward_entry.stake_entry = ctx.accounts.stake_entry.key();
    reward_entry.reward_seconds_received = 0;
    reward_entry.multiplier = ctx.accounts.reward_distributor.default_multiplier;
    Ok(())
}


