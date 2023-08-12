programs/cardinal-stake-pool/src/instructions/stake_booster/update_stake_booster.rs
===================================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct UpdateStakeBoosterIx {
    payment_amount: u64,
    payment_mint: Pubkey,
    payment_manager: Pubkey,
    boost_seconds: u128,
    start_time_seconds: i64,
}

#[derive(Accounts)]
pub struct UpdateStakeBoosterCtx<'info> {
    #[account(mut)]
    stake_booster: Box<Account<'info, StakeBooster>>,
    #[account(mut, constraint = stake_booster.stake_pool == stake_pool.key() @ ErrorCode::InvalidStakePool)]
    stake_pool: Box<Account<'info, StakePool>>,
    #[account(mut, constraint = authority.key() == stake_pool.authority @ ErrorCode::InvalidAuthority)]
    authority: Signer<'info>,
}

pub fn handler(ctx: Context<UpdateStakeBoosterCtx>, ix: UpdateStakeBoosterIx) -> Result<()> {
    let stake_booster = &mut ctx.accounts.stake_booster;
    assert_stake_boost_payment_manager(&ix.payment_manager)?;
    stake_booster.payment_amount = ix.payment_amount;
    stake_booster.payment_mint = ix.payment_mint;
    stake_booster.boost_seconds = ix.boost_seconds;
    stake_booster.payment_manager = ix.payment_manager;
    stake_booster.start_time_seconds = ix.start_time_seconds;

    Ok(())
}


