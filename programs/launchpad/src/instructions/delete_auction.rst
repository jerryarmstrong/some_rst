programs/launchpad/src/instructions/delete_auction.rs
=====================================================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    //! DeleteAuction instruction handler

use {
    crate::{
        error::LaunchpadError,
        state::{
            self,
            auction::Auction,
            launchpad::Launchpad,
            multisig::{AdminInstruction, Multisig},
        },
    },
    anchor_lang::prelude::*,
    anchor_spl::token::{Token, TokenAccount},
};

#[derive(Accounts)]
pub struct DeleteAuction<'info> {
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
        seeds = [b"auction",
                 auction.common.name.as_bytes()],
        bump = auction.bump,
        close = transfer_authority
    )]
    pub auction: Box<Account<'info, Auction>>,

    token_program: Program<'info, Token>,
    // remaining accounts:
    //   1 to Auction::MAX_TOKENS dispensing custody addresses (write, unsigned)
    //      with seeds = [b"dispense", mint.key().as_ref(), auction.key().as_ref()],
}

#[derive(AnchorSerialize, AnchorDeserialize)]
pub struct DeleteAuctionParams {}

pub fn delete_auction<'info>(
    ctx: Context<'_, '_, '_, 'info, DeleteAuction<'info>>,
    params: &DeleteAuctionParams,
) -> Result<u8> {
    if !cfg!(feature = "test") {
        return err!(LaunchpadError::InvalidEnvironment);
    }

    // validate signatures
    let mut multisig = ctx.accounts.multisig.load_mut()?;

    let signatures_left = multisig.sign_multisig(
        &ctx.accounts.admin,
        &Multisig::get_account_infos(&ctx)[1..],
        &Multisig::get_instruction_data(AdminInstruction::DeleteAuction, params)?,
    )?;
    if signatures_left > 0 {
        msg!(
            "Instruction has been signed but more signatures are required: {}",
            signatures_left
        );
        return Ok(signatures_left);
    }

    let auction = &ctx.accounts.auction;
    if !ctx.remaining_accounts.is_empty() && auction.num_tokens > 0 {
        if ctx.remaining_accounts.len() > auction.num_tokens.into() {
            return err!(LaunchpadError::TooManyAccountKeys);
        }
        if ctx.remaining_accounts.len() < auction.num_tokens.into() {
            return Err(ProgramError::NotEnoughAccountKeys.into());
        }
        let dispensers = state::load_accounts::<TokenAccount>(
            &ctx.remaining_accounts[..auction.num_tokens.into()],
            &Token::id(),
        )?;
        for (i, dispenser) in dispensers.iter().enumerate() {
            require_keys_eq!(
                dispenser.key(),
                auction.tokens[i].account,
                LaunchpadError::InvalidDispenserAddress
            );
            if dispenser.amount > 0 {
                msg!("Non-empty dispensing account: {}", dispenser.key());
                return err!(LaunchpadError::AuctionNotEmpty);
            }
            state::close_token_account(
                ctx.accounts.transfer_authority.to_account_info(),
                ctx.remaining_accounts[i].clone(),
                ctx.accounts.token_program.to_account_info(),
                ctx.accounts.transfer_authority.to_account_info(),
                &[&[
                    b"transfer_authority",
                    &[ctx.accounts.launchpad.transfer_authority_bump],
                ]],
            )?;
        }
    }

    Ok(0)
}


