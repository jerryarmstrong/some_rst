programs/cardinal-stake-pool/src/instructions/deauthorize_mint.rs
=================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct DeauthorizeMintCtx<'info> {
    #[account(mut)]
    stake_pool: Account<'info, StakePool>,
    #[account(mut, close = authority, constraint = stake_authorization_record.pool == stake_pool.key() @ ErrorCode::InvalidStakeAuthorizationRecord)]
    stake_authorization_record: Account<'info, StakeAuthorizationRecord>,
    #[account(mut, constraint = authority.key() == stake_pool.authority @ ErrorCode::InvalidPoolAuthority)]
    authority: Signer<'info>,
}

pub fn handler(_ctx: Context<DeauthorizeMintCtx>) -> Result<()> {
    Ok(())
}


