programs/launchpad/src/state/seller_balance.rs
==============================================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

#[account]
#[derive(Default, Debug)]
pub struct SellerBalance {
    pub owner: Pubkey,
    pub custody: Pubkey,
    pub balance: u64,
    pub bump: u8,
}

impl SellerBalance {
    pub const LEN: usize = 8 + std::mem::size_of::<SellerBalance>();
}


