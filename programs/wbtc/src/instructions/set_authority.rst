programs/wbtc/src/instructions/set_authority.rs
===============================================

Last edited: 2023-06-16 20:26:13

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

use crate::error::ErrorCode;
use crate::state::Config;

#[derive(Accounts)]
pub struct SetAuthorityAccounts<'info> {
    #[account(mut)]
    pub authority: Signer<'info>,

    #[account(mut, has_one = authority @ ErrorCode::InvalidAuthority)]
    pub config: Account<'info, Config>,

    /// CHECK: nothing to check here, its just the new authority address
    #[account(constraint = new_authority.key() != config.custodian @ ErrorCode::InvalidNewAuthority)]
    pub new_authority: AccountInfo<'info>,
}

pub fn handler(ctx: Context<SetAuthorityAccounts>) -> Result<()> {
    ctx.accounts.config.new_authority = ctx.accounts.new_authority.key();

    Ok(())
}


