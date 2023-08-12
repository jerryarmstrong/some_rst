tests/typescript/programs/typescript/src/lib.rs
===============================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    //! The typescript example serves to show how one would setup an Anchor
//! workspace with TypeScript tests and migrations.

use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod typescript {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}


