programs/cardinal-stake-pool/src/instructions/stake_pool_fill_zeros.rs
======================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct StakePoolFillZeros<'info> {
    #[account(mut)]
    stake_pool: Account<'info, StakePool>,
}

pub fn handler(ctx: Context<StakePoolFillZeros>) -> Result<()> {
    let stake_pool = &mut ctx.accounts.stake_pool;
    let stake_pool_account = stake_pool.to_account_info();
    let mut stake_pool_data = stake_pool_account.data.borrow_mut();
    let len = stake_pool_data.len();
    stake_pool_data[stake_pool.try_to_vec()?.len()..len].iter_mut().for_each(|d| *d = 0);
    Ok(())
}


