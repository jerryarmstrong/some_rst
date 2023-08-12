programs/cardinal-stake-pool/src/instructions/groups/remove_from_group_entry.rs
===============================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use crate::utils::resize_account;
use anchor_lang::prelude::*;
use anchor_lang::AccountsClose;

#[derive(Accounts)]
pub struct RemoveFromGroupEntryCtx<'info> {
    #[account(mut, has_one = authority)]
    group_entry: Box<Account<'info, GroupStakeEntry>>,

    #[account(mut, constraint = stake_entry.last_staker == authority.key() @ ErrorCode::InvalidAuthority)]
    stake_entry: Box<Account<'info, StakeEntry>>,

    #[account(mut)]
    authority: Signer<'info>,
    #[account(mut)]
    payer: Signer<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<RemoveFromGroupEntryCtx>) -> Result<()> {
    let group_entry = &mut ctx.accounts.group_entry;
    let stake_entry = &mut ctx.accounts.stake_entry;

    if stake_entry.grouped != Some(true) {
        return Err(error!(ErrorCode::UngroupedStakeEntry));
    }
    if group_entry.group_cooldown_start_seconds.is_none() || ((Clock::get().unwrap().unix_timestamp - group_entry.group_cooldown_start_seconds.unwrap()) as u32) < group_entry.group_cooldown_seconds {
        return Err(error!(ErrorCode::CooldownSecondRemaining));
    }

    stake_entry.grouped = Some(false);

    if let Some(index) = group_entry.stake_entries.iter().position(|value| *value == stake_entry.key()) {
        group_entry.stake_entries.remove(index);
    } else {
        return Err(error!(ErrorCode::StakeEntryNotFoundInGroup));
    }

    if group_entry.stake_entries.is_empty() {
        group_entry.close(ctx.accounts.payer.to_account_info())?;
    } else {
        let new_space = group_entry.try_to_vec()?.len() + 8;
        resize_account(
            &group_entry.to_account_info(),
            new_space,
            &ctx.accounts.payer.to_account_info(),
            &ctx.accounts.system_program.to_account_info(),
        )?;
    }
    Ok(())
}


