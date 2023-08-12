programs/cardinal-stake-pool/src/instructions/groups/init_ungrouping.rs
=======================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use crate::utils::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct InitUngroupingCtx<'info> {
    #[account(mut, has_one = authority)]
    group_entry: Box<Account<'info, GroupStakeEntry>>,

    #[account(mut)]
    authority: Signer<'info>,
    #[account(mut)]
    payer: Signer<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<InitUngroupingCtx>) -> Result<()> {
    let group_entry = &mut ctx.accounts.group_entry;

    if group_entry.group_stake_seconds > 0 && (Clock::get().unwrap().unix_timestamp - group_entry.changed_at) < group_entry.group_stake_seconds as i64 {
        return Err(error!(ErrorCode::MinGroupSecondsNotSatisfied));
    }

    if group_entry.group_cooldown_start_seconds.is_some() {
        return Err(error!(ErrorCode::CooldownSecondRemaining));
    }

    group_entry.group_cooldown_start_seconds = Some(Clock::get().unwrap().unix_timestamp);

    let new_space = group_entry.try_to_vec()?.len() + 8;

    resize_account(
        &group_entry.to_account_info(),
        new_space,
        &ctx.accounts.payer.to_account_info(),
        &ctx.accounts.system_program.to_account_info(),
    )?;

    Ok(())
}


