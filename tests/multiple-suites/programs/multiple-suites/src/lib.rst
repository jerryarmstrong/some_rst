tests/multiple-suites/programs/multiple-suites/src/lib.rs
=========================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod multiple_suites {
    use super::*;

    // _val to ensure tx are different so they don't get rejected.
    pub fn initialize(_ctx: Context<Initialize>, _val: u64) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}


