programs/launchpad/src/instructions/update_auction.rs
=====================================================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    //! UpdateAuction instruction handler

use {
    crate::{
        error::LaunchpadError,
        state::{
            self,
            auction::{Auction, CommonParams, PaymentParams, PricingParams},
            launchpad::Launchpad,
        },
    },
    anchor_lang::prelude::*,
};

#[derive(Accounts)]
pub struct UpdateAuction<'info> {
    #[account(mut)]
    pub owner: Signer<'info>,

    /// CHECK: empty PDA, authority for token accounts
    #[account(
        mut,
        seeds = [b"transfer_authority"],
        bump = launchpad.transfer_authority_bump
    )]
    pub transfer_authority: AccountInfo<'info>,

    #[account(
        mut,
        seeds = [b"launchpad"],
        bump = launchpad.launchpad_bump
    )]
    pub launchpad: Box<Account<'info, Launchpad>>,

    #[account(
        mut,
        has_one = owner,
        seeds = [b"auction",
                 auction.common.name.as_bytes()],
        bump = auction.bump
    )]
    pub auction: Box<Account<'info, Auction>>,

    system_program: Program<'info, System>,
}

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct UpdateAuctionParams {
    pub common: CommonParams,
    pub payment: PaymentParams,
    pub pricing: PricingParams,
    pub token_ratios: Vec<u64>,
}

pub fn update_auction(ctx: Context<UpdateAuction>, params: &UpdateAuctionParams) -> Result<()> {
    require!(
        ctx.accounts.launchpad.permissions.allow_auction_updates,
        LaunchpadError::AuctionUpdatesNotAllowed
    );

    // collect fee
    let launchpad = ctx.accounts.launchpad.as_mut();
    state::transfer_sol(
        ctx.accounts.owner.to_account_info(),
        ctx.accounts.transfer_authority.to_account_info(),
        ctx.accounts.system_program.to_account_info(),
        launchpad.fees.auction_update,
    )?;
    launchpad.collected_fees.auction_update_sol = launchpad
        .collected_fees
        .auction_update_sol
        .wrapping_add(launchpad.fees.auction_update);

    // update auction data
    let auction = ctx.accounts.auction.as_mut();

    require!(auction.updatable, LaunchpadError::AuctionNotUpdatable);

    auction.common = params.common.clone();
    auction.payment = params.payment;
    auction.pricing = params.pricing;

    for n in 0..(auction.num_tokens as usize) {
        auction.tokens[n].ratio = params.token_ratios[n];
    }

    auction.update_time = auction.get_time()?;

    if !auction.validate()? {
        err!(LaunchpadError::InvalidAuctionConfig)
    } else {
        Ok(())
    }
}


