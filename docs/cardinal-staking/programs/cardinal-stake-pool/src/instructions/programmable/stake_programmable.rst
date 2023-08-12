programs/cardinal-stake-pool/src/instructions/programmable/stake_programmable.rs
================================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use crate::state::*;
use crate::ID;
use anchor_lang::prelude::*;
use anchor_lang::{AccountsExit, Discriminator, InstructionData};
use anchor_spl::token::Mint;
use anchor_spl::token::Token;
use anchor_spl::token::TokenAccount;
use mpl_token_metadata::instruction::DelegateArgs;
use mpl_token_metadata::instruction::LockArgs;
use mpl_token_metadata::instruction::MetadataInstruction;
use mpl_token_metadata::state::Metadata;
use mpl_token_metadata::utils::assert_derivation;
use solana_program::instruction::Instruction;
use solana_program::program::invoke;
use solana_program::program::invoke_signed;
use solana_program::pubkey;

pub const REWARD_DISTRIBUTOR_PROGRAM: Pubkey = pubkey!("H2yQahQ7eQH8HXXPtJSJn8MURRFEWVesTd8PsracXp1S");

#[derive(Accounts)]
pub struct StakeProgrammableCtx<'info> {
    #[account(
        init_if_needed,
        seeds = [
            STAKE_ENTRY_PREFIX.as_bytes(),
            stake_pool.key().as_ref(),
            original_mint.key().as_ref(),
            get_stake_seed(original_mint.supply, user.key()).as_ref()
        ],
        payer = user,
        space = STAKE_ENTRY_SIZE,
        bump
    )]
    stake_entry: Box<Account<'info, StakeEntry>>,

    /// CHECK: Checked in CPI
    #[account(mut)]
    reward_entry: UncheckedAccount<'info>,
    /// CHECK: Checked in CPI
    #[account(mut)]
    reward_distributor: UncheckedAccount<'info>,

    #[account(mut)]
    stake_pool: Box<Account<'info, StakePool>>,

    original_mint: Box<Account<'info, Mint>>,

    // user
    #[account(mut)]
    user: Signer<'info>,
    #[account(mut, constraint =
    user_original_mint_token_account.amount > 0
    && user_original_mint_token_account.mint == original_mint.key()
    && user_original_mint_token_account.owner == user.key()
    @ ErrorCode::InvalidUserOriginalMintTokenAccount
    )]
    user_original_mint_token_account: Box<Account<'info, TokenAccount>>,
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

    token_program: Program<'info, Token>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    #[account(address = mpl_token_metadata::id())]
    token_metadata_program: UncheckedAccount<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    authorization_rules_program: UncheckedAccount<'info>,

    /// CHECK: constraint check.
    #[account(constraint = reward_distributor_program.key() == REWARD_DISTRIBUTOR_PROGRAM)]
    reward_distributor_program: UncheckedAccount<'info>,
    system_program: Program<'info, System>,
}

pub fn handler(ctx: Context<StakeProgrammableCtx>, amount: u64) -> Result<()> {
    let stake_pool = &mut ctx.accounts.stake_pool;
    let stake_entry = &mut ctx.accounts.stake_entry;

    if stake_entry.bump == 0 {
        stake_entry.bump = *ctx.bumps.get("stake_entry").unwrap();
        stake_entry.pool = stake_pool.key();
        stake_entry.original_mint = ctx.accounts.original_mint.key();
        stake_entry.amount = 0;
        // Write the account data here. We need to do this manually because
        // anchor operates over a copy of the data, while the
        // cardinal_reward_distributor program needs to have the mutated
        // data.
        {
            stake_entry.exit(&ID)?;
        }

        // assert metadata account derivation
        assert_derivation(
            &mpl_token_metadata::id(),
            &ctx.accounts.mint_metadata.to_account_info(),
            &[
                mpl_token_metadata::state::PREFIX.as_bytes(),
                mpl_token_metadata::id().as_ref(),
                ctx.accounts.original_mint.key().as_ref(),
            ],
        )?;
        // check allowlist
        if !stake_pool.requires_creators.is_empty() || !stake_pool.requires_collections.is_empty() || stake_pool.requires_authorization {
            let mut allowed = false;

            if !ctx.accounts.mint_metadata.data_is_empty() {
                let mint_metadata_data = ctx.accounts.mint_metadata.try_borrow_mut_data().expect("Failed to borrow data");
                if ctx.accounts.mint_metadata.to_account_info().owner.key() != mpl_token_metadata::id() {
                    return Err(error!(ErrorCode::InvalidMintMetadataOwner));
                }
                let mint_metadata = Metadata::deserialize(&mut mint_metadata_data.as_ref()).expect("Failed to deserialize metadata");
                if mint_metadata.mint != ctx.accounts.original_mint.key() {
                    return Err(error!(ErrorCode::InvalidMintMetadata));
                }

                if !stake_pool.requires_creators.is_empty() && mint_metadata.data.creators.is_some() {
                    let creators = mint_metadata.data.creators.unwrap();
                    let find = creators.iter().find(|c| stake_pool.requires_creators.contains(&c.address) && c.verified);
                    if find.is_some() {
                        allowed = true
                    };
                }

                if !stake_pool.requires_collections.is_empty() && mint_metadata.collection.is_some() {
                    let collection = mint_metadata.collection.unwrap();
                    if collection.verified && stake_pool.requires_collections.contains(&collection.key) {
                        allowed = true
                    }
                }
            }

            if stake_pool.requires_authorization && !allowed {
                let remaining_accs = &mut ctx.remaining_accounts.iter();
                let stake_entry_authorization_info = next_account_info(remaining_accs)?;
                let stake_entry_authorization_account = match Account::<StakeAuthorizationRecord>::try_from(stake_entry_authorization_info) {
                    Ok(record) => record,
                    Err(_) => return Err(error!(ErrorCode::InvalidStakeAuthorizationRecord)),
                };
                if stake_entry_authorization_account.pool == stake_entry.pool && stake_entry_authorization_account.mint == stake_entry.original_mint {
                    allowed = true;
                }
            }
            if !allowed {
                return Err(error!(ErrorCode::MintNotAllowedInPool));
            }

            //
            // invocation to
            // cardinal_reward_distributor::cpi::init_reward_entry.
            //
            // We use this manual invocation to avoid a circular crate dependency
            // As the published version of the crate has the wrong program id.
            //
            // Alternatively: we could just publish our own. Instead, we do this.
            //
            invoke(
                &Instruction {
                    program_id: REWARD_DISTRIBUTOR_PROGRAM,
                    accounts: vec![
                        AccountMeta::new(ctx.accounts.reward_entry.key(), false),
                        AccountMeta::new_readonly(stake_entry.key(), false),
                        AccountMeta::new(ctx.accounts.reward_distributor.key(), false),
                        AccountMeta::new(ctx.accounts.user.key(), true),
                        AccountMeta::new_readonly(ctx.accounts.system_program.key(), false),
                    ],
                    // WARNING: if the instruction interface ever changes
                    //          this is not going to work, because this is
                    //          using a published crate for the instruction data.
                    //          Not ideal but this is done to avoid a circular
                    //          dependnecy.
                    data: cardinal_reward_distributor::instruction::InitRewardEntry.data(),
                },
                &[
                    ctx.accounts.reward_entry.to_account_info(),
                    stake_entry.to_account_info(),
                    ctx.accounts.reward_distributor.to_account_info(),
                    ctx.accounts.user.to_account_info(),
                    ctx.accounts.system_program.to_account_info(),
                ],
            )?;
        }
    }

    let seed = get_stake_seed(ctx.accounts.original_mint.supply, ctx.accounts.user.key());
    let original_mint = stake_entry.original_mint;
    let stake_pool_id = stake_entry.pool;
    let stake_entry_seed = [STAKE_ENTRY_PREFIX.as_bytes(), stake_pool_id.as_ref(), original_mint.as_ref(), seed.as_ref(), &[stake_entry.bump]];
    let stake_entry_signer = &[&stake_entry_seed[..]];

    if stake_pool.end_date.is_some() && Clock::get().unwrap().unix_timestamp > stake_pool.end_date.unwrap() {
        return Err(error!(ErrorCode::StakePoolHasEnded));
    }

    if stake_entry.amount != 0 {
        stake_entry.total_stake_seconds = stake_entry.total_stake_seconds.saturating_add(
            (u128::try_from(stake_entry.cooldown_start_seconds.unwrap_or(Clock::get().unwrap().unix_timestamp))
                .unwrap()
                .saturating_sub(u128::try_from(stake_entry.last_updated_at.unwrap_or(stake_entry.last_staked_at)).unwrap()))
            .checked_mul(u128::try_from(stake_entry.amount).unwrap())
            .unwrap(),
        );
        stake_entry.cooldown_start_seconds = None;
    }

    if stake_pool.reset_on_stake && stake_entry.amount == 0 {
        stake_entry.total_stake_seconds = 0;
    }

    // update stake entry
    stake_entry.last_staked_at = Clock::get().unwrap().unix_timestamp;
    stake_entry.last_updated_at = Some(Clock::get().unwrap().unix_timestamp);
    stake_entry.last_staker = ctx.accounts.user.key();
    stake_entry.amount = stake_entry.amount.checked_add(amount).unwrap();
    stake_pool.total_staked = stake_pool.total_staked.checked_add(1).expect("Add error");

    invoke(
        &Instruction {
            program_id: mpl_token_metadata::id(),
            accounts: vec![
                // 0. `[writable]` Delegate record account
                AccountMeta::new_readonly(mpl_token_metadata::id(), false),
                // 1. `[]` Delegated owner
                AccountMeta::new_readonly(stake_entry.key(), false),
                // 2. `[writable]` Metadata account
                AccountMeta::new(ctx.accounts.mint_metadata.key(), false),
                // 3. `[optional]` Master Edition account
                AccountMeta::new_readonly(ctx.accounts.mint_edition.key(), false),
                // 4. `[]` Token record
                AccountMeta::new(ctx.accounts.user_original_mint_token_record.key(), false),
                // 5. `[]` Mint account
                AccountMeta::new_readonly(ctx.accounts.original_mint.key(), false),
                // 6. `[optional, writable]` Token account
                AccountMeta::new(ctx.accounts.user_original_mint_token_account.key(), false),
                // 7. `[signer]` Approver (update authority or token owner) to approve the delegation
                AccountMeta::new_readonly(ctx.accounts.user.key(), true),
                // 8. `[signer, writable]` Payer
                AccountMeta::new(ctx.accounts.user.key(), true),
                // 9. `[]` System Program
                AccountMeta::new_readonly(ctx.accounts.system_program.key(), false),
                // 10. `[]` Instructions sysvar account
                AccountMeta::new_readonly(ctx.accounts.sysvar_instructions.key(), false),
                // 11. `[optional]` SPL Token Program
                AccountMeta::new_readonly(ctx.accounts.token_program.key(), false),
                // 12. `[optional]` Token Authorization Rules program
                AccountMeta::new_readonly(ctx.accounts.authorization_rules_program.key(), false),
                // 13. `[optional]` Token Authorization Rules account
                AccountMeta::new_readonly(ctx.accounts.authorization_rules.key(), false),
            ],
            data: MetadataInstruction::Delegate(DelegateArgs::StakingV1 {
                amount: stake_entry.amount,
                authorization_data: None,
            })
            .try_to_vec()
            .unwrap(),
        },
        &[
            stake_entry.to_account_info(),
            ctx.accounts.mint_metadata.to_account_info(),
            ctx.accounts.mint_edition.to_account_info(),
            ctx.accounts.user_original_mint_token_record.to_account_info(),
            ctx.accounts.original_mint.to_account_info(),
            ctx.accounts.user_original_mint_token_account.to_account_info(),
            ctx.accounts.user.to_account_info(),
            ctx.accounts.system_program.to_account_info(),
            ctx.accounts.sysvar_instructions.to_account_info(),
            ctx.accounts.token_program.to_account_info(),
            ctx.accounts.authorization_rules_program.to_account_info(),
            ctx.accounts.authorization_rules.to_account_info(),
        ],
    )?;

    invoke_signed(
        &Instruction {
            program_id: mpl_token_metadata::id(),
            accounts: vec![
                // 0. `[signer]` Delegate
                AccountMeta::new_readonly(stake_entry.key(), true),
                // 1. `[optional]` Token owner
                AccountMeta::new_readonly(ctx.accounts.user.key(), false),
                // 2. `[writable]` Token account
                AccountMeta::new(ctx.accounts.user_original_mint_token_account.key(), false),
                // 3. `[]` Mint account
                AccountMeta::new_readonly(ctx.accounts.original_mint.key(), false),
                // 4. `[writable]` Metadata account
                AccountMeta::new(ctx.accounts.mint_metadata.key(), false),
                // 5. `[optional]` Edition account
                AccountMeta::new_readonly(ctx.accounts.mint_edition.key(), false),
                // 6. `[optional, writable]` Token record account
                AccountMeta::new(ctx.accounts.user_original_mint_token_record.key(), false),
                // 7. `[signer, writable]` Payer
                AccountMeta::new(ctx.accounts.user.key(), true),
                // 8. `[]` System Program
                AccountMeta::new_readonly(ctx.accounts.system_program.key(), false),
                // 9. `[]` Instructions sysvar account
                AccountMeta::new_readonly(ctx.accounts.sysvar_instructions.key(), false),
                // 10. `[optional]` SPL Token Program
                AccountMeta::new_readonly(ctx.accounts.token_program.key(), false),
                // 11. `[optional]` Token Authorization Rules program
                AccountMeta::new_readonly(ctx.accounts.authorization_rules_program.key(), false),
                // 12. `[optional]` Token Authorization Rules account
                AccountMeta::new_readonly(ctx.accounts.authorization_rules.key(), false),
            ],
            data: MetadataInstruction::Lock(LockArgs::V1 { authorization_data: None }).try_to_vec().unwrap(),
        },
        &[
            stake_entry.to_account_info(),
            ctx.accounts.user.to_account_info(),
            ctx.accounts.user_original_mint_token_account.to_account_info(),
            ctx.accounts.original_mint.to_account_info(),
            ctx.accounts.mint_metadata.to_account_info(),
            ctx.accounts.mint_edition.to_account_info(),
            ctx.accounts.user_original_mint_token_record.to_account_info(),
            ctx.accounts.system_program.to_account_info(),
            ctx.accounts.sysvar_instructions.to_account_info(),
            ctx.accounts.token_program.to_account_info(),
            ctx.accounts.authorization_rules_program.to_account_info(),
            ctx.accounts.authorization_rules.to_account_info(),
        ],
        stake_entry_signer,
    )?;

    Ok(())
}


