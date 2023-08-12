programs/cardinal-stake-pool/src/lib.rs
=======================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    pub mod errors;
pub mod instructions;
pub mod state;
pub mod utils;

use anchor_lang::prelude::*;
use instructions::*;

declare_id!("2gvBmibwtBnbkLExmgsijKy6hGXJneou8X6hkyWQvYnF");

#[program]
pub mod cardinal_stake_pool {

    use super::*;

    pub fn init_identifier(ctx: Context<InitIdentifierCtx>) -> Result<()> {
        init_identifier::handler(ctx)
    }

    pub fn init_pool(ctx: Context<InitPoolCtx>, ix: InitPoolIx) -> Result<()> {
        init_pool::handler(ctx, ix)
    }

    pub fn stake_programmable(ctx: Context<StakeProgrammableCtx>, amount: u64) -> Result<()> {
        programmable::stake_programmable::handler(ctx, amount)
    }

    pub fn unstake_programmable(ctx: Context<UnstakeProgrammableCtx>) -> Result<()> {
        programmable::unstake_programmable::handler(ctx)
    }

    pub fn update_total_stake_seconds(ctx: Context<UpdateTotalStakeSecondsCtx>) -> Result<()> {
        update_total_stake_seconds::handler(ctx)
    }

    // pub fn init_entry(ctx: Context<InitEntryCtx>, user: Pubkey) -> Result<()> {
    //     init_entry::handler(ctx, user)
    // }

    // pub fn stake(ctx: Context<StakeCtx>, amount: u64) -> Result<()> {
    //     stake::handler(ctx, amount)
    // }

    // pub fn unstake(ctx: Context<UnstakeCtx>) -> Result<()> {
    //     unstake::handler(ctx)
    // }

    // pub fn init_stake_mint(ctx: Context<InitStakeMintCtx>, ix: InitStakeMintIx) -> Result<()> {
    //     init_stake_mint::handler(ctx, ix)
    // }

    // pub fn authorize_mint(ctx: Context<AuthorizeMintCtx>, mint: Pubkey) -> Result<()> {
    //     authorize_mint::handler(ctx, mint)
    // }

    // pub fn deauthorize_mint(ctx: Context<DeauthorizeMintCtx>) -> Result<()> {
    //     deauthorize_mint::handler(ctx)
    // }

    // pub fn claim_receipt_mint<'key, 'accounts, 'remaining, 'info>(ctx: Context<'key, 'accounts, 'remaining, 'info, ClaimReceiptMintCtx<'info>>) -> Result<()> {
    //     claim_receipt_mint::handler(ctx)
    // }

    // pub fn update_pool(ctx: Context<UpdatePoolCtx>, ix: UpdatePoolIx) -> Result<()> {
    //     update_pool::handler(ctx, ix)
    // }

    // pub fn return_receipt_mint<'key, 'accounts, 'remaining, 'info>(ctx: Context<'key, 'accounts, 'remaining, 'info, ReturnReceiptMintCtx<'info>>) -> Result<()> {
    //     return_receipt_mint::handler(ctx)
    // }

    // pub fn close_stake_pool(ctx: Context<CloseStakePoolCtx>) -> Result<()> {
    //     close_stake_pool::handler(ctx)
    // }

    // pub fn close_stake_entry(ctx: Context<CloseStakeEntryCtx>) -> Result<()> {
    //     close_stake_entry::handler(ctx)
    // }

    // pub fn stake_entry_fill_zeros(ctx: Context<StakeEntryFillZeros>) -> Result<()> {
    //     stake_entry_fill_zeros::handler(ctx)
    // }

    // pub fn stake_entry_resize(ctx: Context<StakeEntryResize>) -> Result<()> {
    //     stake_entry_resize::handler(ctx)
    // }

    // pub fn stake_pool_fill_zeros(ctx: Context<StakePoolFillZeros>) -> Result<()> {
    //     stake_pool_fill_zeros::handler(ctx)
    // }

    // pub fn reassign_stake_entry(ctx: Context<ReassignStakeEntryCtx>, ix: ReassignStakeEntryIx) -> Result<()> {
    //     reassign_stake_entry::handler(ctx, ix)
    // }

    // pub fn double_or_reset_total_stake_seconds(ctx: Context<DoubleOrResetTotalStakeSecondsCtx>) -> Result<()> {
    //     double_or_reset_total_stake_seconds::handler(ctx)
    // }

    // pub fn claim_stake_entry_funds(ctx: Context<ClaimStakeEntryFundsCtx>) -> Result<()> {
    //     claim_stake_entry_funds::handler(ctx)
    // }

    // pub fn reset_stake_entry_bump(ctx: Context<ResetStakeEntryBumpCtx>) -> Result<()> {
    //     reset_stake_entry_bump::handler(ctx)
    // }

    // //// programmable ////

    // pub fn unstake_custodial_programmable(ctx: Context<UnstakeCustodialProgrammableCtx>) -> Result<()> {
    //     programmable::unstake_custodial_programmable::handler(ctx)
    // }

    // //// stake_booster ////
    // pub fn init_stake_booster(ctx: Context<InitStakeBoosterCtx>, ix: InitStakeBoosterIx) -> Result<()> {
    //     stake_booster::init_stake_booster::handler(ctx, ix)
    // }

    // pub fn update_stake_booster(ctx: Context<UpdateStakeBoosterCtx>, ix: UpdateStakeBoosterIx) -> Result<()> {
    //     stake_booster::update_stake_booster::handler(ctx, ix)
    // }

    // pub fn boost_stake_entry(ctx: Context<BoostStakeEntryCtx>, ix: BoostStakeEntryIx) -> Result<()> {
    //     stake_booster::boost_stake_entry::handler(ctx, ix)
    // }

    // pub fn close_stake_booster(ctx: Context<CloseStakeBoosterCtx>) -> Result<()> {
    //     stake_booster::close_stake_booster::handler(ctx)
    // }

    // //// groups ////
    // pub fn init_group_entry(ctx: Context<InitGroupEntryCtx>, ix: InitGroupEntryIx) -> Result<()> {
    //     groups::init_group_entry::handler(ctx, ix)
    // }

    // pub fn add_to_group_entry(ctx: Context<AddToGroupEntryCtx>) -> Result<()> {
    //     groups::add_to_group_entry::handler(ctx)
    // }

    // pub fn remove_from_group_entry(ctx: Context<RemoveFromGroupEntryCtx>) -> Result<()> {
    //     groups::remove_from_group_entry::handler(ctx)
    // }

    // pub fn init_ungrouping(ctx: Context<InitUngroupingCtx>) -> Result<()> {
    //     groups::init_ungrouping::handler(ctx)
    // }
}


