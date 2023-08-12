programs/cardinal-stake-pool/src/instructions/double_or_reset_total_stake_seconds.rs
====================================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;
use arrayref::array_ref;
use solana_program::sysvar::{self};

#[derive(Accounts)]
pub struct DoubleOrResetTotalStakeSecondsCtx<'info> {
    #[account(mut)]
    stake_entry: Account<'info, StakeEntry>,

    #[account(mut, constraint = stake_entry.pool == stake_pool.key() && stake_pool.double_or_reset_enabled.expect("Double or reset not set") @ ErrorCode::InvalidStakePool)]
    stake_pool: Account<'info, StakePool>,

    #[account(constraint = stake_entry.last_staker == last_staker.key() @ ErrorCode::InvalidLastStaker)]
    last_staker: Signer<'info>,
    /// CHECK: account constraints checked in account trait
    #[account(address = sysvar::slot_hashes::id())]
    recent_slothashes: UncheckedAccount<'info>,
}

pub fn handler(ctx: Context<DoubleOrResetTotalStakeSecondsCtx>) -> Result<()> {
    let stake_entry = &mut ctx.accounts.stake_entry;
    let recent_slothashes = &ctx.accounts.recent_slothashes;
    let recent_slothashes_data = recent_slothashes.data.borrow();
    let recent_slothash = array_ref![recent_slothashes_data, 12, 8];
    let timestamp = Clock::get()?.unix_timestamp;
    let pseudo_random_num = u64::from_le_bytes(*recent_slothash).saturating_sub(timestamp.try_into().expect("Conversion error"));

    if stake_entry.cooldown_start_seconds.is_none() {
        stake_entry.total_stake_seconds = stake_entry.total_stake_seconds.saturating_add(
            (u128::try_from(stake_entry.cooldown_start_seconds.unwrap_or(Clock::get().unwrap().unix_timestamp))
                .unwrap()
                .saturating_sub(u128::try_from(stake_entry.last_updated_at.unwrap_or(stake_entry.last_staked_at)).unwrap()))
            .checked_mul(u128::try_from(stake_entry.amount).unwrap())
            .unwrap(),
        );
        stake_entry.last_updated_at = Some(Clock::get().unwrap().unix_timestamp);
    }

    if pseudo_random_num % 2 == 0 {
        stake_entry.total_stake_seconds = stake_entry.total_stake_seconds.checked_mul(2).expect("Mul error");
    } else {
        stake_entry.total_stake_seconds = 0;
    };
    Ok(())
}


