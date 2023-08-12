programs/cardinal-stake-pool/src/instructions/unstake.rs
========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;
use anchor_spl::token::Mint;
use anchor_spl::token::Token;
use anchor_spl::token::TokenAccount;
use anchor_spl::token::{self};

#[derive(Accounts)]
pub struct UnstakeCtx<'info> {
    #[account(mut)]
    stake_pool: Box<Account<'info, StakePool>>,
    #[account(mut, constraint = stake_entry.pool == stake_pool.key() @ ErrorCode::InvalidStakePool)]
    stake_entry: Box<Account<'info, StakeEntry>>,

    original_mint: Box<Account<'info, Mint>>,

    // stake_entry token accounts
    #[account(mut, constraint =
        (stake_entry_original_mint_token_account.amount > 0 || stake_pool.cooldown_seconds.is_some() || stake_pool.min_stake_seconds.is_some())
        && stake_entry_original_mint_token_account.mint == stake_entry.original_mint
        && stake_entry_original_mint_token_account.owner == stake_entry.key()
        @ ErrorCode::InvalidStakeEntryOriginalMintTokenAccount)]
    stake_entry_original_mint_token_account: Box<Account<'info, TokenAccount>>,

    // user
    #[account(mut, constraint = user.key() == stake_entry.last_staker @ ErrorCode::InvalidUnstakeUser)]
    user: Signer<'info>,
    #[account(mut, constraint =
        user_original_mint_token_account.mint == stake_entry.original_mint
        && user_original_mint_token_account.owner == user.key()
        @ ErrorCode::InvalidUserOriginalMintTokenAccount)]
    user_original_mint_token_account: Box<Account<'info, TokenAccount>>,

    // programs
    token_program: Program<'info, Token>,
}

pub fn handler(ctx: Context<UnstakeCtx>) -> Result<()> {
    let stake_pool = &mut ctx.accounts.stake_pool;
    let stake_entry = &mut ctx.accounts.stake_entry;

    let seed = get_stake_seed(ctx.accounts.original_mint.supply, ctx.accounts.user.key());
    let original_mint = stake_entry.original_mint;
    let stake_pool_id = stake_pool.key();
    let stake_entry_seed = [STAKE_ENTRY_PREFIX.as_bytes(), stake_pool_id.as_ref(), original_mint.as_ref(), seed.as_ref(), &[stake_entry.bump]];
    let stake_entry_signer = &[&stake_entry_seed[..]];

    if stake_entry.grouped == Some(true) {
        return Err(error!(ErrorCode::GroupedStakeEntry));
    }

    if stake_pool.min_stake_seconds.is_some()
        && stake_pool.min_stake_seconds.unwrap() > 0
        && ((Clock::get().unwrap().unix_timestamp - stake_entry.last_staked_at) as u32) < stake_pool.min_stake_seconds.unwrap()
    {
        return Err(error!(ErrorCode::MinStakeSecondsNotSatisfied));
    }

    if stake_pool.cooldown_seconds.is_some() && stake_pool.cooldown_seconds.unwrap() > 0 {
        if stake_entry.cooldown_start_seconds.is_none() {
            stake_entry.cooldown_start_seconds = Some(Clock::get().unwrap().unix_timestamp);
            return Ok(());
        } else if stake_entry.cooldown_start_seconds.is_some() && ((Clock::get().unwrap().unix_timestamp - stake_entry.cooldown_start_seconds.unwrap()) as u32) < stake_pool.cooldown_seconds.unwrap() {
            return Err(error!(ErrorCode::CooldownSecondRemaining));
        }
    }

    // If receipt has been minted, ensure it is back in the stake_entry
    if stake_entry.stake_mint.is_some() {
        let remaining_accs = &mut ctx.remaining_accounts.iter();
        let stake_entry_receipt_mint_token_account_info = next_account_info(remaining_accs)?;
        let stake_entry_receipt_mint_token_account = Account::<TokenAccount>::try_from(stake_entry_receipt_mint_token_account_info)?;
        if stake_entry_receipt_mint_token_account.mint != stake_entry.stake_mint.unwrap()
            || stake_entry_receipt_mint_token_account.owner != stake_entry.key()
            || stake_entry_receipt_mint_token_account.amount == 0
        {
            return Err(error!(ErrorCode::InvalidStakeEntryStakeTokenAccount));
        }
    }

    // give back original mint to user
    let cpi_accounts = token::Transfer {
        from: ctx.accounts.stake_entry_original_mint_token_account.to_account_info(),
        to: ctx.accounts.user_original_mint_token_account.to_account_info(),
        authority: stake_entry.to_account_info(),
    };
    let cpi_program = ctx.accounts.token_program.to_account_info();
    let cpi_context = CpiContext::new(cpi_program, cpi_accounts).with_signer(stake_entry_signer);
    token::transfer(cpi_context, stake_entry.amount)?;

    stake_entry.total_stake_seconds = stake_entry.total_stake_seconds.saturating_add(
        (u128::try_from(stake_entry.cooldown_start_seconds.unwrap_or(Clock::get().unwrap().unix_timestamp))
            .unwrap()
            .saturating_sub(u128::try_from(stake_entry.last_updated_at.unwrap_or(stake_entry.last_staked_at)).unwrap()))
        .checked_mul(u128::try_from(stake_entry.amount).unwrap())
        .unwrap(),
    );
    stake_entry.last_updated_at = Some(Clock::get().unwrap().unix_timestamp);
    stake_entry.last_staker = Pubkey::default();
    stake_entry.original_mint_claimed = false;
    stake_entry.stake_mint_claimed = false;
    stake_entry.amount = 0;
    stake_entry.cooldown_start_seconds = None;
    stake_pool.total_staked = stake_pool.total_staked.checked_sub(1).expect("Sub error");
    stake_entry.kind = StakeEntryKind::Permissionless as u8;
    stake_entry_fill_zeros(stake_entry)?;

    Ok(())
}


