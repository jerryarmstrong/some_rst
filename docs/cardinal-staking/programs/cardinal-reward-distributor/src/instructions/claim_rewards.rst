programs/cardinal-reward-distributor/src/instructions/claim_rewards.rs
======================================================================

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
use std::cmp::min;
use std::str::FromStr;

#[derive(Accounts)]
pub struct ClaimRewardsCtx<'info> {
    #[account(mut)]
    reward_entry: Box<Account<'info, RewardEntry>>,
    #[account(mut, constraint = reward_distributor.stake_pool == stake_pool.key() && reward_entry.reward_distributor == reward_distributor.key())]
    reward_distributor: Box<Account<'info, RewardDistributor>>,

    #[account(constraint =
        stake_entry.key() == reward_entry.stake_entry
        && stake_entry.last_staker != Pubkey::default()
        && stake_entry.last_staker == user.key()
        && stake_entry.original_mint == original_mint.key()
        @ ErrorCode::InvalidStakeEntry)]
    stake_entry: Box<Account<'info, StakeEntry>>,
    #[account(constraint = stake_pool.key() == stake_entry.pool)]
    stake_pool: Box<Account<'info, StakePool>>,

    original_mint: Box<Account<'info, Mint>>,
    #[account(mut, constraint = reward_mint.key() == reward_distributor.reward_mint @ ErrorCode::InvalidRewardMint)]
    reward_mint: Box<Account<'info, Mint>>,

    #[account(init_if_needed,
        payer = user,
        associated_token::mint = reward_mint,
        associated_token::authority = authority,
    )]
    user_reward_mint_token_account: Box<Account<'info, TokenAccount>>,

    // Note: the PDA seeds are checked in the handler function body.
    authority: Signer<'info>,
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

pub fn handler<'key, 'accounts, 'remaining, 'info>(ctx: Context<'key, 'accounts, 'remaining, 'info, ClaimRewardsCtx<'info>>) -> Result<()> {
    let reward_entry = &mut ctx.accounts.reward_entry;
    let reward_distributor = &mut ctx.accounts.reward_distributor;
    let stake_pool = reward_distributor.stake_pool;
    let stake_entry = &mut ctx.accounts.stake_entry;
    let reward_distributor_seed = &[REWARD_DISTRIBUTOR_SEED.as_bytes(), stake_pool.as_ref(), &[reward_distributor.bump]];
    let reward_distributor_signer = &[&reward_distributor_seed[..]];

    let authority = &ctx.accounts.authority;
    let original_mint = &ctx.accounts.original_mint;
    let original_mint_key = original_mint.key();
    let expected_authority = Pubkey::find_program_address(
        &[NS_SBA_SCOPED_USER_NFT_PROGRAM, stake_entry.last_staker.as_ref(), original_mint_key.as_ref(), crate::ID.as_ref()],
        &SBA_PROGRAM,
    )
    .0;

    if authority.key() != expected_authority {
        return Err(error!(ErrorCode::InvalidRewardTokenOwner));
    }

    let reward_amount = reward_distributor.reward_amount;
    let reward_duration_seconds = reward_distributor.reward_duration_seconds;

    // if stake_entry.kind == StakeEntryKind::Permissioned as u8
    //     // if someone else updated this users stake_entry then it must be checked that they are still the staker - this should be called BEFORE unstake
    //     && ctx.accounts.user_reward_mint_token_account.owner != stake_entry.last_staker
    //     // can only be signed by the last_staker or the reward distributor authority
    //     && (ctx.accounts.user.key() != stake_entry.last_staker || ctx.accounts.user.key() != reward_distributor.authority)
    // {
    //     return Err(error!(ErrorCode::InvalidUserRewardMintTokenAccount));
    // }

    let reward_seconds_received = reward_entry.reward_seconds_received;
    if reward_seconds_received <= stake_entry.total_stake_seconds && (reward_distributor.max_supply.is_none() || reward_distributor.rewards_issued < reward_distributor.max_supply.unwrap() as u128) {
        let mut reward_seconds = stake_entry.total_stake_seconds;
        if let Some(max_reward_seconds) = reward_distributor.max_reward_seconds_received {
            reward_seconds = min(reward_seconds, max_reward_seconds)
        };
        if reward_distributor.max_reward_seconds_received.is_some() && reward_seconds_received >= reward_seconds {
            return Err(error!(ErrorCode::MaxRewardSecondsClaimed));
        }

        let mut reward_amount_to_receive = reward_seconds
            .checked_sub(reward_seconds_received)
            .unwrap()
            .checked_div(reward_duration_seconds)
            .unwrap()
            .checked_mul(reward_amount as u128)
            .unwrap()
            .checked_mul(reward_entry.multiplier as u128)
            .unwrap()
            .checked_div((10_u128).checked_pow(reward_distributor.multiplier_decimals as u32).unwrap())
            .unwrap();

        // if this will go over max supply give rewards up to max supply
        if reward_distributor.max_supply.is_some() && reward_distributor.rewards_issued.checked_add(reward_amount_to_receive).unwrap() >= reward_distributor.max_supply.unwrap() as u128 {
            reward_amount_to_receive = (reward_distributor.max_supply.unwrap() as u128).checked_sub(reward_distributor.rewards_issued).unwrap();
        }

        // mint to the user
        let remaining_accs = &mut ctx.remaining_accounts.iter();
        match reward_distributor.kind {
            k if k == RewardDistributorKind::Mint as u8 => {
                let cpi_accounts = token::MintTo {
                    mint: ctx.accounts.reward_mint.to_account_info(),
                    to: ctx.accounts.user_reward_mint_token_account.to_account_info(),
                    authority: reward_distributor.to_account_info(),
                };
                let cpi_program = ctx.accounts.token_program.to_account_info();
                let cpi_context = CpiContext::new(cpi_program, cpi_accounts).with_signer(reward_distributor_signer);
                // todo this could be an issue and get stuck, might need 2 transfers
                token::mint_to(cpi_context, reward_amount_to_receive.try_into().expect("Too many rewards to receive"))?;
            }
            k if k == RewardDistributorKind::Treasury as u8 => {
                let reward_distributor_token_account_info = next_account_info(remaining_accs)?;
                let reward_distributor_token_account = Account::<TokenAccount>::try_from(reward_distributor_token_account_info)?;

                if reward_amount_to_receive > reward_distributor_token_account.amount as u128 {
                    reward_amount_to_receive = reward_distributor_token_account.amount as u128;
                }

                let cpi_accounts = token::Transfer {
                    from: reward_distributor_token_account.to_account_info(),
                    to: ctx.accounts.user_reward_mint_token_account.to_account_info(),
                    authority: reward_distributor.to_account_info(),
                };
                let cpi_program = ctx.accounts.token_program.to_account_info();
                let cpi_context = CpiContext::new(cpi_program, cpi_accounts).with_signer(reward_distributor_signer);
                // todo this could be an issue and get stuck, might need 2 transfers
                token::transfer(cpi_context, reward_amount_to_receive.try_into().expect("Too many rewards to receive"))?;
            }
            _ => return Err(error!(ErrorCode::InvalidRewardDistributorKind)),
        }
        // update values
        // this is nuanced about if the rewards are closed, should they get the reward time for that time even though they didnt get any rewards?
        // this only matters if the reward distributor becomes open again and they missed out on some rewards they coudlve gotten
        let reward_time_to_receive = if reward_entry.multiplier != 0 {
            reward_amount_to_receive
                .checked_mul((10_u128).checked_pow(reward_distributor.multiplier_decimals as u32).unwrap())
                .unwrap()
                .checked_div(reward_entry.multiplier as u128)
                .unwrap()
                .checked_div(reward_amount as u128)
                .unwrap()
                .checked_mul(reward_duration_seconds)
                .unwrap()
        } else {
            0_u128
        };

        reward_distributor.rewards_issued = reward_distributor.rewards_issued.checked_add(reward_amount_to_receive).unwrap();
        reward_entry.reward_seconds_received = reward_entry.reward_seconds_received.checked_add(reward_time_to_receive).unwrap();

        // invoke(
        //     &transfer(&ctx.accounts.user.to_account_info().key(), &ctx.accounts.reward_manager.key(), CLAIM_REWARD_LAMPORTS),
        //     &[
        //         ctx.accounts.user.to_account_info(),
        //         ctx.accounts.reward_manager.to_account_info(),
        //         ctx.accounts.system_program.to_account_info(),
        //     ],
        // )?;
    }

    Ok(())
}


