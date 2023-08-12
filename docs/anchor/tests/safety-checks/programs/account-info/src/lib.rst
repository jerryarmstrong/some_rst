tests/safety-checks/programs/account-info/src/lib.rs
====================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod account_info {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    unchecked: AccountInfo<'info>,
}


