programs/cardinal-reward-distributor/src/lib.rs
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    pub mod errors;
pub mod instructions;
pub mod state;

use anchor_lang::prelude::*;
use instructions::*;

declare_id!("H2yQahQ7eQH8HXXPtJSJn8MURRFEWVesTd8PsracXp1S");

#[program]
pub mod cardinal_reward_distributor {
    use super::*;

    pub fn init_reward_distributor<'key, 'accounts, 'remaining, 'info>(ctx: Context<'key, 'accounts, 'remaining, 'info, InitRewardDistributorCtx<'info>>, ix: InitRewardDistributorIx) -> Result<()> {
        init_reward_distributor::handler(ctx, ix)
    }

    pub fn init_reward_entry(ctx: Context<InitRewardEntryCtx>) -> Result<()> {
        init_reward_entry::handler(ctx)
    }

    pub fn claim_rewards<'key, 'accounts, 'remaining, 'info>(ctx: Context<'key, 'accounts, 'remaining, 'info, ClaimRewardsCtx<'info>>) -> Result<()> {
        claim_rewards::handler(ctx)
    }

    pub fn transfer_rewards(ctx: Context<TransferRewardsCtx>, amount: Option<u64>) -> Result<()> {
        transfer_rewards::handler(ctx, amount)
    }

    // pub fn update_reward_entry(ctx: Context<UpdateRewardEntryCtx>, ix: UpdateRewardEntryIx) -> Result<()> {
    //     update_reward_entry::handler(ctx, ix)
    // }

    // pub fn close_reward_distributor<'key, 'accounts, 'remaining, 'info>(ctx: Context<'key, 'accounts, 'remaining, 'info, CloseCtx<'info>>) -> Result<()> {
    //     close_reward_distributor::handler(ctx)
    // }

    // pub fn close_reward_entry(ctx: Context<CloseRewardEntryCtx>) -> Result<()> {
    //     close_reward_entry::handler(ctx)
    // }

    // pub fn update_reward_distributor(ctx: Context<UpdateRewardDistributorCtx>, ix: UpdateRewardDistributorIx) -> Result<()> {
    //     update_reward_distributor::handler(ctx, ix)
    // }

    // pub fn reclaim_funds(ctx: Context<ReclaimFundsCtx>, amount: u64) -> Result<()> {
    //     reclaim_funds::handler(ctx, amount)
    // }
}


