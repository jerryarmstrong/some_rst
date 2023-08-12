programs/launchpad/src/instructions/disable_auction.rs
======================================================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    //! DisableAuction instruction handler

use {crate::state::auction::Auction, anchor_lang::prelude::*};

#[derive(Accounts)]
pub struct DisableAuction<'info> {
    #[account()]
    pub owner: Signer<'info>,

    #[account(
        mut,
        has_one = owner,
        seeds = [b"auction",
                 auction.common.name.as_bytes()],
        bump = auction.bump
    )]
    pub auction: Box<Account<'info, Auction>>,
}

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct DisableAuctionParams {}

pub fn disable_auction(ctx: Context<DisableAuction>, _params: &DisableAuctionParams) -> Result<()> {
    let auction = ctx.accounts.auction.as_mut();
    auction.enabled = false;

    Ok(())
}


