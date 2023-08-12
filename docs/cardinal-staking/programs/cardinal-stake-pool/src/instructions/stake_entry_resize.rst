programs/cardinal-stake-pool/src/instructions/stake_entry_resize.rs
===================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::utils::resize_account;

use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct StakeEntryResize<'info> {
    #[account(mut)]
    stake_entry: Account<'info, StakeEntry>,
    #[account(mut)]
    payer: Signer<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<StakeEntryResize>) -> Result<()> {
    let stake_entry = &mut ctx.accounts.stake_entry;
    resize_account(
        &stake_entry.to_account_info(),
        STAKE_ENTRY_SIZE,
        &ctx.accounts.payer.to_account_info(),
        &ctx.accounts.system_program.to_account_info(),
    )?;
    Ok(())
}


