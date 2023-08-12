programs/candy-guard/program/src/instructions/set_authority.rs
==============================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

use crate::state::CandyGuard;

pub fn set_authority(ctx: Context<SetAuthority>, new_authority: Pubkey) -> Result<()> {
    let candy_guard = &mut ctx.accounts.candy_guard;

    candy_guard.authority = new_authority;

    Ok(())
}

#[derive(Accounts)]
pub struct SetAuthority<'info> {
    #[account(mut, has_one = authority)]
    candy_guard: Account<'info, CandyGuard>,
    authority: Signer<'info>,
}


