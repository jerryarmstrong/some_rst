programs/wbtc/src/instructions/claim_authority.rs
=================================================

Last edited: 2023-06-16 20:26:13

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

use crate::error::ErrorCode;
use crate::state::Config;

#[derive(Accounts)]
pub struct ClaimAuthorityAccounts<'info> {
    #[account(mut)]
    pub new_authority: Signer<'info>,

    #[account(mut, has_one = new_authority @ ErrorCode::InvalidAuthority)]
    pub config: Account<'info, Config>,
}

pub fn handler(ctx: Context<ClaimAuthorityAccounts>) -> Result<()> {
    ctx.accounts.config.authority = ctx.accounts.new_authority.key();
    ctx.accounts.config.new_authority = Pubkey::default();

    Ok(())
}


