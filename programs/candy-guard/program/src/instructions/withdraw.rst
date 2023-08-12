programs/candy-guard/program/src/instructions/withdraw.rs
=========================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

use crate::state::CandyGuard;

pub fn withdraw(_ctx: Context<Withdraw<'_>>) -> Result<()> {
    Ok(())
}

/// Withdraw the rent SOL from the candy guard account.
#[derive(Accounts)]
pub struct Withdraw<'info> {
    #[account(mut, close = authority, has_one = authority)]
    candy_guard: Account<'info, CandyGuard>,
    #[account(mut)]
    authority: Signer<'info>,
}


