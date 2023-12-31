programs/launchpad/src/instructions/withdraw_fees.rs
====================================================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    //! WithdrawFees instruction handler

use {
    crate::{
        error::LaunchpadError,
        math,
        state::{
            self,
            custody::Custody,
            launchpad::Launchpad,
            multisig::{AdminInstruction, Multisig},
        },
    },
    anchor_lang::prelude::*,
    anchor_spl::token::{Token, TokenAccount},
    solana_program::sysvar,
};

#[derive(Accounts)]
pub struct WithdrawFees<'info> {
    #[account()]
    pub admin: Signer<'info>,

    #[account(
        mut,
        seeds = [b"multisig"],
        bump = multisig.load()?.bump
    )]
    pub multisig: AccountLoader<'info, Multisig>,

    /// CHECK: empty PDA, authority for token accounts
    #[account(
        mut,
        seeds = [b"transfer_authority"], 
        bump = launchpad.transfer_authority_bump
    )]
    pub transfer_authority: AccountInfo<'info>,

    #[account(
        seeds = [b"launchpad"],
        bump = launchpad.launchpad_bump
    )]
    pub launchpad: Box<Account<'info, Launchpad>>,

    #[account(
        mut,
        seeds = [b"custody",
                 custody.mint.key().as_ref()],
        bump = custody.bump
    )]
    pub custody: Box<Account<'info, Custody>>,

    #[account(
        mut,
        constraint = custody_token_account.key() == custody.token_account.key()
    )]
    pub custody_token_account: Box<Account<'info, TokenAccount>>,

    #[account(
        mut,
        constraint = receiving_token_account.mint == custody_token_account.mint
    )]
    pub receiving_token_account: Box<Account<'info, TokenAccount>>,

    /// CHECK: SOL fees receiving account
    #[account(
        mut,
        constraint = receiving_sol_account.data_is_empty()
    )]
    pub receiving_sol_account: AccountInfo<'info>,

    token_program: Program<'info, Token>,
}

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct WithdrawFeesParams {
    pub token_amount: u64,
    pub sol_amount: u64,
}

pub fn withdraw_fees<'info>(
    ctx: Context<'_, '_, '_, 'info, WithdrawFees<'info>>,
    params: &WithdrawFeesParams,
) -> Result<u8> {
    // validate inputs
    require!(
        params.token_amount > 0 || params.sol_amount > 0,
        LaunchpadError::InvalidTokenAmount
    );

    // validate signatures
    let mut multisig = ctx.accounts.multisig.load_mut()?;

    let signatures_left = multisig.sign_multisig(
        &ctx.accounts.admin,
        &Multisig::get_account_infos(&ctx)[1..],
        &Multisig::get_instruction_data(AdminInstruction::WithdrawFees, params)?,
    )?;
    if signatures_left > 0 {
        msg!(
            "Instruction has been signed but more signatures are required: {}",
            signatures_left
        );
        return Ok(signatures_left);
    }

    // transfer token fees from the custody to the receiver
    if params.token_amount > 0 {
        let custody = ctx.accounts.custody.as_mut();
        msg!(
            "Withdraw token fees: {} / {}",
            params.token_amount,
            custody.collected_fees
        );
        if custody.collected_fees < params.token_amount {
            return Err(ProgramError::InsufficientFunds.into());
        }
        custody.collected_fees = math::checked_sub(custody.collected_fees, params.token_amount)?;

        ctx.accounts.launchpad.transfer_tokens(
            ctx.accounts.custody_token_account.to_account_info(),
            ctx.accounts.receiving_token_account.to_account_info(),
            ctx.accounts.transfer_authority.to_account_info(),
            ctx.accounts.token_program.to_account_info(),
            params.token_amount,
        )?;
    }

    // transfer sol fees from the custody to the receiver
    if params.sol_amount > 0 {
        let balance = ctx.accounts.transfer_authority.try_lamports()?;
        let min_balance = sysvar::rent::Rent::get().unwrap().minimum_balance(0);
        let available_balance = if balance > min_balance {
            math::checked_sub(balance, min_balance)?
        } else {
            0
        };
        msg!(
            "Withdraw SOL fees: {} / {}",
            params.sol_amount,
            available_balance
        );
        if available_balance < params.sol_amount {
            return Err(ProgramError::InsufficientFunds.into());
        }

        state::transfer_sol_from_owned(
            ctx.accounts.transfer_authority.to_account_info(),
            ctx.accounts.receiving_sol_account.to_account_info(),
            params.sol_amount,
        )?;
    }

    Ok(0)
}


