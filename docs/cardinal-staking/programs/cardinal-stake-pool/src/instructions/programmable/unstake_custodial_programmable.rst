programs/cardinal-stake-pool/src/instructions/programmable/unstake_custodial_programmable.rs
============================================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use anchor_lang::prelude::*;
use anchor_spl::associated_token::AssociatedToken;
use anchor_spl::token::Mint;
use anchor_spl::token::Token;
use anchor_spl::token::TokenAccount;
use mpl_token_metadata::instruction::MetadataInstruction;
use mpl_token_metadata::instruction::TransferArgs;
use solana_program::instruction::Instruction;
use solana_program::program::invoke_signed;

#[derive(Accounts)]
pub struct UnstakeCustodialProgrammableCtx<'info> {
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

    /// CHECK: This is not dangerous because we don't read or write from this account
    #[account(mut)]
    stake_entry_original_mint_token_record: UncheckedAccount<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    #[account(mut)]
    user_original_mint_token_record: UncheckedAccount<'info>,

    /// CHECK: This is not dangerous because we don't read or write from this account
    #[account(mut)]
    mint_metadata: UncheckedAccount<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    mint_edition: UncheckedAccount<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    authorization_rules: UncheckedAccount<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    sysvar_instructions: UncheckedAccount<'info>,

    // programs
    token_program: Program<'info, Token>,
    associated_token_program: Program<'info, AssociatedToken>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    #[account(address = mpl_token_metadata::id())]
    token_metadata_program: UncheckedAccount<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    authorization_rules_program: UncheckedAccount<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<UnstakeCustodialProgrammableCtx>) -> Result<()> {
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

    invoke_signed(
        &Instruction {
            program_id: mpl_token_metadata::id(),
            accounts: vec![
                // #[account(0, writable, name="token", desc="Token account")]
                AccountMeta::new(ctx.accounts.stake_entry_original_mint_token_account.key(), false),
                // #[account(1, name="token_owner", desc="Token account owner")]
                AccountMeta::new_readonly(stake_entry.key(), false),
                // #[account(2, writable, name="destination", desc="Destination token account")]
                AccountMeta::new(ctx.accounts.user_original_mint_token_account.key(), false),
                // #[account(3, name="destination_owner", desc="Destination token account owner")]
                AccountMeta::new_readonly(ctx.accounts.user.key(), false),
                // #[account(4, name="mint", desc="Mint of token asset")]
                AccountMeta::new_readonly(original_mint.key(), false),
                // #[account(5, writable, name="metadata", desc="Metadata (pda of ['metadata', program id, mint id])")]
                AccountMeta::new(ctx.accounts.mint_metadata.key(), false),
                // #[account(6, optional, name="edition", desc="Edition of token asset")]
                AccountMeta::new_readonly(ctx.accounts.mint_edition.key(), false),
                // #[account(7, optional, writable, name="recipient_token_record", desc="Owner token record account")]
                AccountMeta::new(ctx.accounts.stake_entry_original_mint_token_record.key(), false),
                // #[account(8, optional, writable, name="destination_token_record", desc="Destination token record account")]
                AccountMeta::new(ctx.accounts.user_original_mint_token_record.key(), false),
                // #[account(9, signer, name="authority", desc="Transfer authority (token owner or delegate)")]
                AccountMeta::new_readonly(stake_entry.key(), true),
                // #[account(10, signer, writable, name="payer", desc="Payer")]
                AccountMeta::new(ctx.accounts.user.key(), true),
                // #[account(11, name="system_program", desc="System Program")]
                AccountMeta::new_readonly(ctx.accounts.system_program.key(), false),
                // #[account(12, name="sysvar_instructions", desc="Instructions sysvar account")]
                AccountMeta::new_readonly(ctx.accounts.sysvar_instructions.key(), false),
                // #[account(13, name="spl_token_program", desc="SPL Token Program")]
                AccountMeta::new_readonly(ctx.accounts.token_program.key(), false),
                // #[account(14, name="spl_ata_program", desc="SPL Associated Token Account program")]
                AccountMeta::new_readonly(ctx.accounts.associated_token_program.key(), false),
                // #[account(15, optional, name="authorization_rules_program", desc="Token Authorization Rules Program")]
                AccountMeta::new_readonly(ctx.accounts.authorization_rules_program.key(), false),
                // #[account(16, optional, name="authorization_rules", desc="Token Authorization Rules account")]
                AccountMeta::new_readonly(ctx.accounts.authorization_rules.key(), false),
            ],
            data: MetadataInstruction::Transfer(TransferArgs::V1 {
                amount: stake_entry.amount,
                authorization_data: None,
            })
            .try_to_vec()
            .unwrap(),
        },
        &[
            ctx.accounts.stake_entry_original_mint_token_account.to_account_info(),
            stake_entry.to_account_info(),
            ctx.accounts.user_original_mint_token_account.to_account_info(),
            ctx.accounts.user.to_account_info(),
            ctx.accounts.original_mint.to_account_info(),
            ctx.accounts.mint_metadata.to_account_info(),
            ctx.accounts.mint_edition.to_account_info(),
            ctx.accounts.stake_entry_original_mint_token_record.to_account_info(),
            ctx.accounts.user_original_mint_token_record.to_account_info(),
            ctx.accounts.user.to_account_info(),
            ctx.accounts.system_program.to_account_info(),
            ctx.accounts.sysvar_instructions.to_account_info(),
            ctx.accounts.token_program.to_account_info(),
            ctx.accounts.associated_token_program.to_account_info(),
            ctx.accounts.authorization_rules_program.to_account_info(),
            ctx.accounts.authorization_rules.to_account_info(),
        ],
        stake_entry_signer,
    )?;

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


