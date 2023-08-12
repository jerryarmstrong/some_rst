programs/cardinal-stake-pool/src/instructions/claim_stake_entry_funds.rs
========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use anchor_spl::token::Mint;
use anchor_spl::token::Token;
use anchor_spl::token::TokenAccount;
use anchor_spl::token::{self};

use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;

#[derive(Accounts)]
pub struct ClaimStakeEntryFundsCtx<'info> {
    funds_mint: Box<Account<'info, Mint>>,
    #[account(mut, constraint = stake_entry_funds_mint_token_account.owner == stake_entry.key() && stake_entry_funds_mint_token_account.mint == funds_mint.key() @ ErrorCode::InvalidMintForTokenAccount)]
    stake_entry_funds_mint_token_account: Box<Account<'info, TokenAccount>>,
    #[account(mut, constraint = user_funds_mint_token_account.owner == stake_entry.last_staker && user_funds_mint_token_account.mint == funds_mint.key() @ ErrorCode::InvalidMintForTokenAccount)]
    user_funds_mint_token_account: Box<Account<'info, TokenAccount>>,

    stake_pool: Box<Account<'info, StakePool>>,
    #[account(mut, constraint = stake_entry.pool == stake_pool.key() @ ErrorCode::InvalidStakePool)]
    stake_entry: Box<Account<'info, StakeEntry>>,
    #[account(mut, constraint = original_mint.key() == stake_entry.original_mint @ ErrorCode::InvalidOriginalMint)]
    original_mint: Box<Account<'info, Mint>>,

    #[account(mut, constraint = authority.key() == stake_entry.last_staker || authority.key() == stake_pool.authority @ ErrorCode::InvalidAuthority)]
    authority: Signer<'info>,

    token_program: Program<'info, Token>,
}

pub fn handler(ctx: Context<ClaimStakeEntryFundsCtx>) -> Result<()> {
    if ctx.accounts.stake_entry.last_staker == Pubkey::default() {
        return Err(error!(ErrorCode::InvalidLastStaker));
    }

    if let Some(stake_mint) = ctx.accounts.stake_entry.stake_mint {
        if stake_mint == ctx.accounts.funds_mint.key() {
            return Err(error!(ErrorCode::InvalidFundsMint));
        }
    }

    if ctx.accounts.stake_entry_funds_mint_token_account.amount == 0 {
        return Err(error!(ErrorCode::StakeEntryFundsTokenAccountEmpty));
    }

    let stake_pool_key = ctx.accounts.stake_pool.key();
    let seed = get_stake_seed(ctx.accounts.original_mint.supply, ctx.accounts.stake_entry.last_staker);
    let stake_entry_seed = [
        STAKE_ENTRY_PREFIX.as_bytes(),
        stake_pool_key.as_ref(),
        ctx.accounts.stake_entry.original_mint.as_ref(),
        seed.as_ref(),
        &[ctx.accounts.stake_entry.bump],
    ];
    let stake_entry_signer = &[&stake_entry_seed[..]];

    let cpi_accounts = token::Transfer {
        from: ctx.accounts.stake_entry_funds_mint_token_account.to_account_info(),
        to: ctx.accounts.user_funds_mint_token_account.to_account_info(),
        authority: ctx.accounts.stake_entry.to_account_info(),
    };
    let cpi_program = ctx.accounts.token_program.to_account_info();
    let cpi_context = CpiContext::new(cpi_program, cpi_accounts).with_signer(stake_entry_signer);
    token::transfer(cpi_context, ctx.accounts.stake_entry_funds_mint_token_account.amount)?;

    Ok(())
}


