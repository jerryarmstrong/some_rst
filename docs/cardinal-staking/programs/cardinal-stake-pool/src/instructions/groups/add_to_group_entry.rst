programs/cardinal-stake-pool/src/instructions/groups/add_to_group_entry.rs
==========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use crate::utils::resize_account;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct AddToGroupEntryCtx<'info> {
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

pub fn handler(ctx: Context<AddToGroupEntryCtx>) -> Result<()> {
    let group_entry = &mut ctx.accounts.group_entry;
    let stake_entry = &mut ctx.accounts.stake_entry;

    if group_entry.group_cooldown_start_seconds.is_some() {
        return Err(error!(ErrorCode::CooldownSecondRemaining));
    }
    if stake_entry.grouped == Some(true) {
        return Err(error!(ErrorCode::GroupedStakeEntry));
    }
    stake_entry.grouped = Some(true);

    let mut stake_entries = group_entry.stake_entries.clone();
    stake_entries.push(stake_entry.key());

    let new_group_entry = GroupStakeEntry {
        bump: group_entry.bump,
        group_id: group_entry.group_id,
        authority: group_entry.authority,
        stake_entries: stake_entries.to_vec(),
        changed_at: Clock::get().unwrap().unix_timestamp,
        group_cooldown_seconds: group_entry.group_cooldown_seconds,
        group_stake_seconds: group_entry.group_stake_seconds,
        group_cooldown_start_seconds: None,
    };
    let new_space = new_group_entry.try_to_vec()?.len() + 8;
    group_entry.set_inner(new_group_entry);

    resize_account(
        &group_entry.to_account_info(),
        new_space,
        &ctx.accounts.payer.to_account_info(),
        &ctx.accounts.system_program.to_account_info(),
    )?;

    let new_stake_entry = StakeEntry {
        bump: stake_entry.bump,
        pool: stake_entry.pool,
        amount: stake_entry.amount,
        original_mint: stake_entry.original_mint,
        original_mint_claimed: stake_entry.original_mint_claimed,
        last_staker: stake_entry.last_staker,
        last_staked_at: stake_entry.last_staked_at,
        total_stake_seconds: stake_entry.total_stake_seconds,
        stake_mint_claimed: stake_entry.stake_mint_claimed,
        kind: stake_entry.kind,
        stake_mint: stake_entry.stake_mint,
        cooldown_start_seconds: stake_entry.cooldown_start_seconds,
        last_updated_at: stake_entry.last_updated_at,
        grouped: stake_entry.grouped,
    };
    let new_space = new_stake_entry.try_to_vec()?.len() + 8;
    stake_entry.set_inner(new_stake_entry);

    resize_account(
        &stake_entry.to_account_info(),
        new_space,
        &ctx.accounts.payer.to_account_info(),
        &ctx.accounts.system_program.to_account_info(),
    )?;

    Ok(())
}


