tests/anchor-cli-idl/programs/idl-commands-one/src/lib.rs
=========================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

declare_id!("2uA3amp95zsEHUpo8qnLMhcFAUsiKVEcKHXS1JetFjU5");

#[program]
pub mod idl_commands_one {
    use super::*;

    pub fn initialize(_ctx: Context<Initialize>) -> Result<()> {
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}


