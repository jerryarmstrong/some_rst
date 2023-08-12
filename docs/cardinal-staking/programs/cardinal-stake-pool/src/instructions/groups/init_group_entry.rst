programs/cardinal-stake-pool/src/instructions/groups/init_group_entry.rs
========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::state::*;
use anchor_lang::prelude::*;

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct InitGroupEntryIx {
    pub group_id: Pubkey,
    pub group_cooldown_seconds: Option<u32>,
    pub group_stake_seconds: Option<u32>,
}

#[derive(Accounts)]
#[instruction(ix: InitGroupEntryIx)]
pub struct InitGroupEntryCtx<'info> {
    #[account(
        init,
        payer = authority,
        space = GROUP_ENTRY_DEFAULT_SIZE,
        seeds = [GROUP_ENTRY_PREFIX.as_bytes(), ix.group_id.key().as_ref()],
        bump,
    )]
    group_entry: Box<Account<'info, GroupStakeEntry>>,
    #[account(mut)]
    authority: Signer<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<InitGroupEntryCtx>, ix: InitGroupEntryIx) -> Result<()> {
    let group_entry = &mut ctx.accounts.group_entry;
    let authority = &mut ctx.accounts.authority;
    group_entry.bump = *ctx.bumps.get("group_entry").unwrap();
    group_entry.group_id = ix.group_id;
    group_entry.authority = authority.key();
    group_entry.changed_at = Clock::get().unwrap().unix_timestamp;
    group_entry.group_cooldown_seconds = ix.group_cooldown_seconds.unwrap_or(0);
    group_entry.group_stake_seconds = ix.group_stake_seconds.unwrap_or(0);

    Ok(())
}


