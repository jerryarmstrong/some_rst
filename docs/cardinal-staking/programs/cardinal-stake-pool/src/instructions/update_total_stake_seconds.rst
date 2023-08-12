programs/cardinal-stake-pool/src/instructions/update_total_stake_seconds.rs
===========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct UpdateTotalStakeSecondsCtx<'info> {
    #[account(mut, constraint = stake_entry.last_staker != Pubkey::default() @ ErrorCode::CannotUpdateUnstakedEntry)]
    stake_entry: Account<'info, StakeEntry>,

    #[account(mut)]
    last_staker: Signer<'info>,
}

pub fn handler(ctx: Context<UpdateTotalStakeSecondsCtx>) -> Result<()> {
    let stake_entry = &mut ctx.accounts.stake_entry;

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

    // if ctx.accounts.last_staker.key() != stake_entry.last_staker {
    //     stake_entry.kind = StakeEntryKind::Permissioned as u8
    // }
    Ok(())
}


