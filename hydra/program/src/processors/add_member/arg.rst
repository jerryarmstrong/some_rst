hydra/program/src/processors/add_member/arg.rs
==============================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

#[derive(AnchorSerialize, AnchorDeserialize, Clone, Default)]
pub struct AddMemberArgs {
    pub shares: u64,
}


