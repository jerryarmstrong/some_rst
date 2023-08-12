tests/anchor-cli-idl/programs/idl-commands-two/src/lib.rs
=========================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

declare_id!("DE4UbHnAcT6Kfh1fVTPRPwpiA3vipmQ4xR3gcLwX3wwS");

#[program]
pub mod idl_commands_two {
    use super::*;

    pub fn uninitialize(_ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}


