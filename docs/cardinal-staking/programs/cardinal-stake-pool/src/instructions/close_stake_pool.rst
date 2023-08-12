programs/cardinal-stake-pool/src/instructions/close_stake_pool.rs
=================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;
use anchor_lang::AccountsClose;

#[derive(Accounts)]
pub struct CloseStakePoolCtx<'info> {
    #[account(mut)]
    stake_pool: Box<Account<'info, StakePool>>,
    #[account(mut, constraint = stake_pool.authority == authority.key() @ ErrorCode::InvalidAuthority)]
    authority: Signer<'info>,
}

pub fn handler(ctx: Context<CloseStakePoolCtx>) -> Result<()> {
    let stake_pool = &ctx.accounts.stake_pool;
    if stake_pool.total_staked > 0 {
        return Err(error!(ErrorCode::CannotClosePoolWithStakedEntries));
    }
    ctx.accounts.stake_pool.close(ctx.accounts.authority.to_account_info())?;

    Ok(())
}


