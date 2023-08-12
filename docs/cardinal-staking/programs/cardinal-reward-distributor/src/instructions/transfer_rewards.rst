programs/cardinal-reward-distributor/src/instructions/transfer_rewards.rs
=========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program::invoke;
use anchor_lang::solana_program::system_instruction::transfer;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::Mint;
use anchor_spl::token::Token;
use anchor_spl::token::TokenAccount;
use anchor_spl::token::{self};
use cardinal_stake_pool::state::StakeEntry;
use cardinal_stake_pool::state::StakeEntryKind;
use cardinal_stake_pool::state::StakePool;
use std::str::FromStr;

#[derive(Accounts)]
pub struct TransferRewardsCtx<'info> {
    #[account(mut, constraint = reward_entry_a.reward_distributor == reward_distributor.key())]
    reward_entry_a: Box<Account<'info, RewardEntry>>,
    #[account(mut, constraint = reward_entry_b.key() != reward_entry_a.key()
    && reward_entry_b.reward_distributor == reward_distributor.key())]
    reward_entry_b: Box<Account<'info, RewardEntry>>,
    #[account(mut, constraint = reward_distributor.stake_pool == stake_pool.key())]
    reward_distributor: Box<Account<'info, RewardDistributor>>,

    #[account(constraint =
        stake_entry_a.key() == reward_entry_a.stake_entry
        && stake_entry_a.last_staker == user.key()
        && stake_entry_a.original_mint == original_mint_a.key()
        @ ErrorCode::InvalidStakeEntry)]
    stake_entry_a: Box<Account<'info, StakeEntry>>,
    #[account(constraint =
        stake_entry_b.key() == reward_entry_b.stake_entry
        && stake_entry_b.last_staker == user.key()
        && stake_entry_b.original_mint == original_mint_b.key()
        @ ErrorCode::InvalidStakeEntry)]
    stake_entry_b: Box<Account<'info, StakeEntry>>,
    #[account(constraint = stake_pool.key() == stake_entry_a.pool && stake_pool.key() == stake_entry_b.pool)]
    stake_pool: Box<Account<'info, StakePool>>,

    original_mint_a: Box<Account<'info, Mint>>,
    original_mint_b: Box<Account<'info, Mint>>,
    #[account(mut, constraint = reward_mint.key() == reward_distributor.reward_mint @ ErrorCode::InvalidRewardMint)]
    reward_mint: Box<Account<'info, Mint>>,

    #[account(init_if_needed,
        payer = user,
        associated_token::mint = reward_mint,
        associated_token::authority = authority_a,
    )]
    user_reward_mint_token_account_a: Box<Account<'info, TokenAccount>>,
    #[account(init_if_needed,
        payer = user,
        associated_token::mint = reward_mint,
        associated_token::authority = authority_b,
    )]
    user_reward_mint_token_account_b: Box<Account<'info, TokenAccount>>,

    authority_a: Signer<'info>,

    /// CHECK: PDA checked in handler.
    authority_b: UncheckedAccount<'info>,
    /// CHECK: Authority is checked to be the correct soulbound PDA, which
    ///        is a function of the mint and the last staker, and the last
    ///        staker is indeed this user.
    #[account(mut)]
    user: UncheckedAccount<'info>,
    associated_token_program: Program<'info, AssociatedToken>,
    token_program: Program<'info, Token>,
    system_program: Program<'info, System>,
    rent: Sysvar<'info, Rent>,
}

pub fn handler(ctx: Context<TransferRewardsCtx>, amount: Option<u64>) -> Result<()> {
    let authority_a = &ctx.accounts.authority_a;
    let original_mint_a = &ctx.accounts.original_mint_a;
    let expected_authority_a = Pubkey::find_program_address(
        &[
            NS_SBA_SCOPED_USER_NFT_PROGRAM,
            ctx.accounts.stake_entry_a.last_staker.as_ref(),
            original_mint_a.key().as_ref(),
            crate::ID.as_ref(),
        ],
        &SBA_PROGRAM,
    )
    .0;

    let authority_b = &ctx.accounts.authority_b;
    let original_mint_b = &ctx.accounts.original_mint_b;
    let expected_authority_b = Pubkey::find_program_address(
        &[
            NS_SBA_SCOPED_USER_NFT_PROGRAM,
            ctx.accounts.stake_entry_b.last_staker.as_ref(),
            original_mint_b.key().as_ref(),
            crate::ID.as_ref(),
        ],
        &SBA_PROGRAM,
    )
    .0;

    if authority_a.key() != expected_authority_a || authority_b.key() != expected_authority_b {
        return Err(error!(ErrorCode::InvalidRewardTokenOwner));
    }

    let token_account_a = &ctx.accounts.user_reward_mint_token_account_a;

    let amount = amount.unwrap_or_else(|| token_account_a.amount);
    if amount > token_account_a.amount {
        return Err(error!(ErrorCode::NotEnoughRewardTokens));
    }

    let cpi_accounts = token::Transfer {
        from: ctx.accounts.user_reward_mint_token_account_a.to_account_info(),
        to: ctx.accounts.user_reward_mint_token_account_b.to_account_info(),
        authority: authority_a.to_account_info(),
    };

    let cpi_program = ctx.accounts.token_program.to_account_info();
    let cpi_context = CpiContext::new(cpi_program, cpi_accounts);

    token::transfer(cpi_context, amount)?;

    Ok(())
}


