programs/launchpad/src/instructions/get_auction_amount.rs
=========================================================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    //! GetAuctionAmount instruction handler

use {
    crate::state::{auction::Auction, launchpad::Launchpad},
    anchor_lang::prelude::*,
};

#[derive(Accounts)]
pub struct GetAuctionAmount<'info> {
    #[account()]
    pub user: Signer<'info>,

    #[account(
        seeds = [b"launchpad"], 
        bump = launchpad.launchpad_bump
    )]
    pub launchpad: Box<Account<'info, Launchpad>>,

    #[account(
        seeds = [b"auction",
                 auction.common.name.as_bytes()],
        bump = auction.bump
    )]
    pub auction: Box<Account<'info, Auction>>,
}

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct GetAuctionAmountParams {
    price: u64,
}

pub fn get_auction_amount(
    ctx: Context<GetAuctionAmount>,
    params: &GetAuctionAmountParams,
) -> Result<u64> {
    ctx.accounts
        .auction
        .get_auction_amount(params.price, ctx.accounts.auction.get_time()?)
}


