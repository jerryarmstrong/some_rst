programs/candy-machine-core/program/src/instructions/withdraw.rs
================================================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

use crate::CandyMachine;

pub fn withdraw(_ctx: Context<Withdraw>) -> Result<()> {
    Ok(())
}

/// Withdraw the rent SOL from the candy machine account.
#[derive(Accounts)]
pub struct Withdraw<'info> {
    /// Candy Machine acccount.
    #[account(mut, close = authority, has_one = authority)]
    candy_machine: Account<'info, CandyMachine>,

    /// Authority of the candy machine.
    #[account(mut)]
    authority: Signer<'info>,
}


