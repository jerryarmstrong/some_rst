tests/validator-clone/programs/validator-clone/src/lib.rs
=========================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod validator_clone {
    use super::*;

    pub fn initialize(_ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}


