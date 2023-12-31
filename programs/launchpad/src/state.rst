programs/launchpad/src/state.rs
===============================

Last edited: 2022-12-01 03:09:25

Contents:

.. code-block:: rs

    // Program state handling.

pub mod auction;
pub mod bid;
pub mod custody;
pub mod launchpad;
pub mod multisig;
pub mod oracle;
pub mod seller_balance;

use {
    crate::{error::LaunchpadError, math, state::bid::Bid},
    anchor_lang::{prelude::*, Discriminator},
    anchor_spl::token::{Mint, TokenAccount},
};

pub fn is_empty_account(account_info: &AccountInfo) -> Result<bool> {
    Ok(account_info.try_data_is_empty()? || account_info.try_lamports()? == 0)
}

pub fn initialize_account<'info>(
    payer: AccountInfo<'info>,
    target_account: AccountInfo<'info>,
    system_program: AccountInfo<'info>,
    owner: &Pubkey,
    seeds: &[&[&[u8]]],
    len: usize,
) -> Result<()> {
    let current_lamports = target_account.try_lamports()?;
    if current_lamports == 0 {
        // if account doesn't have any lamports initialize it with conventional create_account
        let lamports = Rent::get()?.minimum_balance(len);
        let cpi_accounts = anchor_lang::system_program::CreateAccount {
            from: payer,
            to: target_account,
        };
        let cpi_context = anchor_lang::context::CpiContext::new(system_program, cpi_accounts);
        anchor_lang::system_program::create_account(
            cpi_context.with_signer(seeds),
            lamports,
            math::checked_as_u64(len)?,
            owner,
        )?;
    } else {
        // fund the account for rent exemption
        let required_lamports = Rent::get()?
            .minimum_balance(len)
            .saturating_sub(current_lamports);
        if required_lamports > 0 {
            let cpi_accounts = anchor_lang::system_program::Transfer {
                from: payer,
                to: target_account.clone(),
            };
            let cpi_context =
                anchor_lang::context::CpiContext::new(system_program.clone(), cpi_accounts);
            anchor_lang::system_program::transfer(cpi_context, required_lamports)?;
        }
        // allocate space
        let cpi_accounts = anchor_lang::system_program::Allocate {
            account_to_allocate: target_account.clone(),
        };
        let cpi_context =
            anchor_lang::context::CpiContext::new(system_program.clone(), cpi_accounts);
        anchor_lang::system_program::allocate(
            cpi_context.with_signer(seeds),
            math::checked_as_u64(len)?,
        )?;
        // assign to the program
        let cpi_accounts = anchor_lang::system_program::Assign {
            account_to_assign: target_account,
        };
        let cpi_context = anchor_lang::context::CpiContext::new(system_program, cpi_accounts);
        anchor_lang::system_program::assign(cpi_context.with_signer(seeds), owner)?;
    }
    Ok(())
}

#[allow(clippy::too_many_arguments)]
pub fn initialize_token_account<'info>(
    payer: AccountInfo<'info>,
    token_account: AccountInfo<'info>,
    mint: AccountInfo<'info>,
    system_program: AccountInfo<'info>,
    token_program: AccountInfo<'info>,
    rent: AccountInfo<'info>,
    authority: AccountInfo<'info>,
    seeds: &[&[&[u8]]],
) -> Result<()> {
    initialize_account(
        payer,
        token_account.clone(),
        system_program.clone(),
        &anchor_spl::token::ID,
        seeds,
        TokenAccount::LEN,
    )?;

    let cpi_accounts = anchor_spl::token::InitializeAccount {
        account: token_account,
        mint,
        authority,
        rent,
    };
    let cpi_context = anchor_lang::context::CpiContext::new(token_program, cpi_accounts);
    anchor_spl::token::initialize_account(cpi_context.with_signer(seeds))
}

pub fn close_token_account<'info>(
    receiver: AccountInfo<'info>,
    token_account: AccountInfo<'info>,
    token_program: AccountInfo<'info>,
    authority: AccountInfo<'info>,
    seeds: &[&[&[u8]]],
) -> Result<()> {
    let cpi_accounts = anchor_spl::token::CloseAccount {
        account: token_account,
        destination: receiver,
        authority,
    };
    let cpi_context = anchor_lang::context::CpiContext::new(token_program, cpi_accounts);
    anchor_spl::token::close_account(cpi_context.with_signer(seeds))
}

pub fn load_accounts<'a, T: AccountSerialize + AccountDeserialize + Owner + Clone>(
    accounts: &[AccountInfo<'a>],
    expected_owner: &Pubkey,
) -> Result<Vec<Account<'a, T>>> {
    let mut res: Vec<Account<T>> = Vec::with_capacity(accounts.len());

    for account in accounts {
        if account.owner != expected_owner {
            return Err(ProgramError::IllegalOwner.into());
        }
        res.push(Account::<T>::try_from(account)?);
    }

    if res.is_empty() {
        return Err(ProgramError::NotEnoughAccountKeys.into());
    }

    Ok(res)
}

pub fn save_accounts<T: AccountSerialize + AccountDeserialize + Owner + Clone>(
    accounts: &[Account<T>],
) -> Result<()> {
    for account in accounts {
        account.exit(&crate::ID)?;
    }
    Ok(())
}

pub fn create_bid_accounts<'a>(
    accounts: &[AccountInfo<'a>],
    owners: &[Pubkey],
    payer: AccountInfo<'a>,
    auction: &Pubkey,
    system_program: AccountInfo<'a>,
) -> Result<Vec<Account<'a, Bid>>> {
    let mut res: Vec<Account<Bid>> = Vec::with_capacity(accounts.len());

    for (bid_account, owner) in accounts.iter().zip(owners) {
        // validate bid address
        let (expected_bid_key, bump) =
            Pubkey::find_program_address(&[b"bid", owner.as_ref(), auction.as_ref()], &crate::ID);
        require_keys_eq!(
            bid_account.key(),
            expected_bid_key,
            LaunchpadError::InvalidBidAddress
        );
        // initialize the account or check the owner
        let mut initialized = false;
        if bid_account.data_is_empty() {
            initialize_account(
                payer.clone(),
                bid_account.clone(),
                system_program.clone(),
                &crate::ID,
                &[&[b"bid", owner.key().as_ref(), auction.as_ref(), &[bump]]],
                Bid::LEN,
            )?;
            let mut bid_data = bid_account.try_borrow_mut_data()?;
            bid_data[..8].copy_from_slice(Bid::discriminator().as_slice());
            initialized = true;
        } else if bid_account.owner != &crate::ID {
            return Err(ProgramError::IllegalOwner.into());
        }

        let mut bid = Account::<Bid>::try_from(bid_account)?;
        if initialized {
            bid.owner = *owner;
            bid.auction = *auction;
            bid.seller_initialized = true;
            bid.bump = bump;
        }
        res.push(bid);
    }

    Ok(res)
}

#[allow(clippy::too_many_arguments)]
pub fn create_token_accounts<'a>(
    accounts: &[AccountInfo<'a>],
    mints: &[AccountInfo<'a>],
    authority: AccountInfo<'a>,
    payer: AccountInfo<'a>,
    auction: &Pubkey,
    system_program: AccountInfo<'a>,
    token_program: AccountInfo<'a>,
    rent: AccountInfo<'a>,
) -> Result<Vec<Account<'a, TokenAccount>>> {
    let mut res: Vec<Account<TokenAccount>> = Vec::with_capacity(accounts.len());
    let mut decimals = 0;

    for (token_account, mint) in accounts.iter().zip(mints) {
        // validate token account address
        let (expected_token_account_key, bump) = Pubkey::find_program_address(
            &[b"dispense", mint.key().as_ref(), auction.as_ref()],
            &crate::ID,
        );
        require_keys_eq!(
            token_account.key(),
            expected_token_account_key,
            LaunchpadError::InvalidDispenserAddress
        );
        let mint_data = Account::<Mint>::try_from(mint)?;
        if res.is_empty() {
            decimals = mint_data.decimals;
        } else if decimals != mint_data.decimals {
            return err!(LaunchpadError::InvalidDispenserDecimals);
        }
        // initialize the account or check the owner
        if token_account.data_is_empty() {
            initialize_token_account(
                payer.clone(),
                token_account.clone(),
                mint.clone(),
                system_program.clone(),
                token_program.clone(),
                rent.clone(),
                authority.clone(),
                &[&[b"dispense", mint.key().as_ref(), auction.as_ref(), &[bump]]],
            )?;
        } else if token_account.owner != &anchor_spl::token::ID {
            return Err(ProgramError::IllegalOwner.into());
        }
        res.push(Account::<TokenAccount>::try_from(token_account)?);
    }

    Ok(res)
}

pub fn transfer_sol_from_owned<'a>(
    program_owned_source_account: AccountInfo<'a>,
    destination_account: AccountInfo<'a>,
    amount: u64,
) -> Result<()> {
    if amount == 0 {
        return Ok(());
    }

    **destination_account.try_borrow_mut_lamports()? = destination_account
        .try_lamports()?
        .checked_add(amount)
        .ok_or(ProgramError::InsufficientFunds)?;
    let source_balance = program_owned_source_account.try_lamports()?;
    if source_balance < amount {
        msg!(
            "Error: Not enough funds to withdraw {} lamports from {}",
            amount,
            program_owned_source_account.key
        );
        return Err(ProgramError::InsufficientFunds.into());
    }
    **program_owned_source_account.try_borrow_mut_lamports()? = source_balance
        .checked_sub(amount)
        .ok_or(ProgramError::InsufficientFunds)?;

    Ok(())
}

pub fn transfer_sol<'a>(
    source_account: AccountInfo<'a>,
    destination_account: AccountInfo<'a>,
    system_program: AccountInfo<'a>,
    amount: u64,
) -> Result<()> {
    if source_account.try_lamports()? < amount {
        msg!(
            "Error: Not enough funds to withdraw {} lamports from {}",
            amount,
            source_account.key
        );
        return Err(ProgramError::InsufficientFunds.into());
    }

    let cpi_accounts = anchor_lang::system_program::Transfer {
        from: source_account,
        to: destination_account,
    };
    let cpi_context = anchor_lang::context::CpiContext::new(system_program, cpi_accounts);
    anchor_lang::system_program::transfer(cpi_context, amount)
}


