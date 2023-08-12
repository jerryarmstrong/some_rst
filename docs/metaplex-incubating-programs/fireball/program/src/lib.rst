fireball/program/src/lib.rs
===========================

Last edited: 2022-04-29 15:13:47

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;
use anchor_spl::token::{self};

use mpl_token_metadata::{
    instruction::{
        mint_new_edition_from_master_edition_via_token,
    },
    utils::{
        create_or_allocate_account_raw,
        puffed_out_string,
    },
};

use solana_program::{
    program::{
        invoke_signed,
    },
};

pub mod merkle_proof;

declare_id!("fireo2tXc3j1Es8GjsGUf6whnEPte8oUvdDz4U2zN9n");

pub const PREFIX: &[u8] = b"fireball";
pub const MAX_URI_LENGTH : usize = 200; // smaller?

fn incomplete_dish_checks<'info>(
    dish: &Account<'info, Dish>,
    payer: &Signer<'info>,
) -> Result<()> {
    require!(
        !dish.completed,
        ErrorCode::RecipeAlreadyCompleted,
    );

    require!(
        dish.authority == payer.key(),
        ErrorCode::InvalidAuthority,
    );

    Ok(())
}

fn complete_dish_checks<'info>(
    dish: &Account<'info, Dish>,
) -> Result<()> {
    require!(
        dish.completed,
        ErrorCode::RecipeNotCompleted,
    );

    Ok(())
}

#[program]
pub mod fireball {
    use super::*;

    pub fn create_recipes(
        ctx: Context<CreateRecipe>,
        ingredients: String,
        roots: Vec<[u8; 32]>,
    ) -> Result<()> {
        let recipe = &mut ctx.accounts.recipe;

        recipe.authority = *ctx.accounts.authority.key;
        recipe.ingredients = puffed_out_string(&ingredients, MAX_URI_LENGTH);
        recipe.roots = roots;

        Ok(())
    }

    pub fn start_dish(
        ctx: Context<StartDish>,
        _dish_bump: u8,
    ) -> Result<()> {
        let dish = &mut ctx.accounts.dish;

        dish.authority = *ctx.accounts.payer.key;
        dish.recipe = ctx.accounts.recipe.key();
        dish.ingredients_added = 0;
        dish.completed = false;

        Ok(())
    }

    pub fn add_ingredient<'info>(
        ctx: Context<'_, '_, '_, 'info, AddIngredient<'info>>,
        ingredient_bump: u8,
        ingredient_num: u64,
        proof: Vec<[u8; 32]>,
    ) -> Result<()> {
        msg!("entered add_ingredient");
        incomplete_dish_checks(&ctx.accounts.dish, &ctx.accounts.payer)?;

        let recipe = &ctx.accounts.recipe;

        require!(
            ctx.accounts.dish.recipe == recipe.key(),
            ErrorCode::MismatchedRecipe,
        );

        let (transfer_mint_info, data_hash_flags)  = if ctx.remaining_accounts.len() == 0 {
            (ctx.accounts.ingredient_mint.to_account_info(), 0x00)
        } else {
            msg!("checking remaining accounts: {}", ctx.remaining_accounts.len());
            let edition_mint = &ctx.remaining_accounts[0];
            let edition_account = &ctx.remaining_accounts[1].to_account_info();
            let master_edition_account = &ctx.remaining_accounts[2].to_account_info();

            // check that the edition account matches the edition mint
            let _edition_bump = mpl_token_metadata::utils::assert_derivation(
                &mpl_token_metadata::ID,
                edition_account,
                &[
                    mpl_token_metadata::state::PREFIX.as_ref(),
                    mpl_token_metadata::ID.as_ref(),
                    edition_mint.key.as_ref(),
                    mpl_token_metadata::state::EDITION.as_ref(),
                ],
            ).map_err(|_| ErrorCode::DerivedKeyInvalid)?;

            // check that the master edition account matches the ingredient mint
            let _master_edition_bump = mpl_token_metadata::utils::assert_derivation(
                &mpl_token_metadata::ID,
                master_edition_account,
                &[
                    mpl_token_metadata::state::PREFIX.as_ref(),
                    mpl_token_metadata::ID.as_ref(),
                    ctx.accounts.ingredient_mint.key().as_ref(),
                    mpl_token_metadata::state::EDITION.as_ref(),
                ],
            ).map_err(|_| ErrorCode::DerivedKeyInvalid)?;

            let edition = mpl_token_metadata::state::Edition::from_account_info(
                edition_account)?;

            require!(
                edition.edition != 0,
                ErrorCode::EditionZeroInvalid,
            );

            // check that the parent 'master edition' is part of the merkle tree
            require!(
                edition.parent == *master_edition_account.key,
                ErrorCode::MismatchedEditionMint,
            );

            // NB: different offset so this is opt-in
            (edition_mint.to_account_info(), 0x02)
        };

        require!(
            ctx.accounts.from.mint
            == transfer_mint_info.key(),
            ErrorCode::InvalidMint,
        );

        let node = solana_program::keccak::hashv(&[
            &[data_hash_flags],
            &ctx.accounts.ingredient_mint.key().to_bytes(),
        ]);

        require!(
            merkle_proof::verify(proof, recipe.roots[ingredient_num as usize], node.0),
            ErrorCode::InvalidProof,
        );

        let dish_key = ctx.accounts.dish.key();
        let ingredient_bytes = ingredient_num.to_le_bytes();
        let ingredient_store_seeds = [
            PREFIX,
            dish_key.as_ref(),
            &ingredient_bytes,
            &[ingredient_bump],
        ];

        require!(
            Pubkey::create_program_address(
                &ingredient_store_seeds,
                &ID,
            )
            == Ok(ctx.accounts.ingredient_store.key()),
            ErrorCode::InvalidMintPDA,
        );

        create_or_allocate_account_raw(
            ctx.accounts.token_program.key(),
            &ctx.accounts.ingredient_store.to_account_info(),
            &ctx.accounts.rent.to_account_info(),
            &ctx.accounts.system_program.to_account_info(),
            &ctx.accounts.payer.to_account_info(),
            token::TokenAccount::LEN,
            &ingredient_store_seeds,
        )?;

        token::initialize_account(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::InitializeAccount {
                    account: ctx.accounts.ingredient_store.to_account_info(),
                    mint: transfer_mint_info,
                    authority: ctx.accounts.ingredient_store.to_account_info(),
                    rent: ctx.accounts.rent.to_account_info(),
                },
            ),
        )?;

        // we can't burn while we don't know if the dish can be completed...
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.from.to_account_info(),
                    to: ctx.accounts.ingredient_store.to_account_info(),
                    authority: ctx.accounts.payer.to_account_info(),
                },
            ),
            1,
        )?;

        let dish = &mut ctx.accounts.dish;

        dish.ingredients_added = dish.ingredients_added
            .checked_add(1)
            .ok_or(ErrorCode::ArithmeticOverflow)?;

        Ok(())
    }

    pub fn remove_ingredient(
        ctx: Context<RemoveIngredient>,
        ingredient_bump: u8,
        ingredient_num: u64,
    ) -> Result<()> {
        incomplete_dish_checks(&ctx.accounts.dish, &ctx.accounts.payer)?;

        let dish_key = ctx.accounts.dish.key();
        let ingredient_bytes = ingredient_num.to_le_bytes();
        let ingredient_store_seeds = [
            PREFIX,
            dish_key.as_ref(),
            &ingredient_bytes,
            &[ingredient_bump],
        ];

        require!(
            Pubkey::create_program_address(
                &ingredient_store_seeds,
                &ID,
            )
            == Ok(ctx.accounts.ingredient_store.key()),
            ErrorCode::InvalidMintPDA,
        );

        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.ingredient_store.to_account_info(),
                    to: ctx.accounts.to.to_account_info(),
                    authority: ctx.accounts.ingredient_store.to_account_info(),
                },
            )
            .with_signer(&[&ingredient_store_seeds]),
            1,
        )?;

        token::close_account(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::CloseAccount {
                    account: ctx.accounts.ingredient_store.to_account_info(),
                    destination: ctx.accounts.payer.to_account_info(),
                    authority: ctx.accounts.ingredient_store.to_account_info(),
                },
            )
            .with_signer(&[&ingredient_store_seeds]),
        )?;

        let dish = &mut ctx.accounts.dish;

        dish.ingredients_added = dish.ingredients_added
            .checked_sub(1)
            .ok_or(ErrorCode::ArithmeticOverflow)?;

        Ok(())
    }

    pub fn make_dish(
        ctx: Context<MakeDish>,
        recipe_signer_bump: u8,
        edition: u64,
    ) -> Result<()> {
        incomplete_dish_checks(&ctx.accounts.dish, &ctx.accounts.payer)?;

        require!(
            ctx.accounts.dish.recipe
            == ctx.accounts.recipe.key(),
            ErrorCode::MismatchedRecipe,
        );

        require!(
            ctx.accounts.dish.ingredients_added
            == ctx.accounts.recipe.roots.len() as u64,
            ErrorCode::IncompleteRecipe,
        );

        let recipe_key = ctx.accounts.recipe.key();
        let recipe_signer_seeds = [
            PREFIX,
            recipe_key.as_ref(),
            &[recipe_signer_bump],
        ];

        let metadata_infos = [
            ctx.accounts.token_metadata_program.clone(),
            ctx.accounts.metadata_new_metadata.clone(),
            ctx.accounts.metadata_new_edition.clone(),
            ctx.accounts.metadata_master_edition.clone(),
            ctx.accounts.metadata_new_mint.clone(),
            ctx.accounts.metadata_edition_mark_pda.clone(),
            ctx.accounts.metadata_new_mint_authority.to_account_info().clone(),
            ctx.accounts.payer.to_account_info().clone(),
            ctx.accounts.metadata_master_token_owner.to_account_info().clone(),
            ctx.accounts.metadata_master_token_account.clone(),
            ctx.accounts.metadata_new_update_authority.clone(),
            ctx.accounts.metadata_master_metadata.clone(),
            ctx.accounts.metadata_master_mint.clone(),
            ctx.accounts.rent.to_account_info().clone(),
        ];

        invoke_signed(
            &mint_new_edition_from_master_edition_via_token(
                *ctx.accounts.token_metadata_program.key,
                *ctx.accounts.metadata_new_metadata.key,
                *ctx.accounts.metadata_new_edition.key,
                *ctx.accounts.metadata_master_edition.key,
                *ctx.accounts.metadata_new_mint.key,
                *ctx.accounts.metadata_new_mint_authority.key,
                *ctx.accounts.payer.key,
                *ctx.accounts.metadata_master_token_owner.key,
                *ctx.accounts.metadata_master_token_account.key,
                *ctx.accounts.metadata_new_update_authority.key,
                *ctx.accounts.metadata_master_metadata.key,
                *ctx.accounts.metadata_master_mint.key,
                edition,
            ),
            &metadata_infos,
            &[&recipe_signer_seeds],
        )?;

        // could set ingredients_added to 0?
        let dish = &mut ctx.accounts.dish;

        dish.completed = true;

        Ok(())
    }

    pub fn consume_ingredient(
        ctx: Context<ConsumeIngredient>,
        ingredient_bump: u8,
        ingredient_num: u64,
    ) -> Result<()> {
        complete_dish_checks(&ctx.accounts.dish)?;

        // TODO: some other reward configured in recipe?
        let recipe = &ctx.accounts.recipe;
        require!(
            ctx.accounts.dish.recipe == recipe.key(),
            ErrorCode::MismatchedRecipe,
        );

        // anyone can call consume and claim the rent...

        let dish_key = ctx.accounts.dish.key();
        let ingredient_bytes = ingredient_num.to_le_bytes();
        let ingredient_store_seeds = [
            PREFIX,
            dish_key.as_ref(),
            &ingredient_bytes,
            &[ingredient_bump],
        ];

        require!(
            Pubkey::create_program_address(
                &ingredient_store_seeds,
                &ID,
            )
            == Ok(ctx.accounts.ingredient_store.key()),
            ErrorCode::InvalidMintPDA,
        );

        token::burn(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::Burn {
                    mint: ctx.accounts.ingredient_mint.to_account_info(),
                    from: ctx.accounts.ingredient_store.to_account_info(),
                    authority: ctx.accounts.ingredient_store.to_account_info(),
                },
            )
            .with_signer(&[&ingredient_store_seeds]),
            1,
        )?;

        token::close_account(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::CloseAccount {
                    account: ctx.accounts.ingredient_store.to_account_info(),
                    destination: ctx.accounts.payer.to_account_info(),
                    authority: ctx.accounts.ingredient_store.to_account_info(),
                },
            )
            .with_signer(&[&ingredient_store_seeds]),
        )?;

        let dish = &mut ctx.accounts.dish;

        dish.ingredients_added = dish.ingredients_added
            .checked_sub(1)
            .ok_or(ErrorCode::ArithmeticOverflow)?;

        if dish.ingredients_added == 0 {
            dish.completed = false;
        } else {
            complete_dish_checks(&ctx.accounts.dish)?;
        }

        Ok(())
    }

    pub fn reclaim_master_edition(
        ctx: Context<ReclaimMasterEdition>,
        recipe_signer_bump: u8,
    ) -> Result<()> {
        let recipe= &ctx.accounts.recipe;

        require!(
            recipe.authority
            == ctx.accounts.payer.key(),
            ErrorCode::InvalidAuthority,
        );

        let recipe_key = ctx.accounts.recipe.key();
        let recipe_signer_seeds = [
            PREFIX,
            recipe_key.as_ref(),
            &[recipe_signer_bump],
        ];

        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.from.to_account_info(),
                    to: ctx.accounts.to.to_account_info(),
                    authority: ctx.accounts.master_token_owner.to_account_info(),
                },
            )
            .with_signer(&[&recipe_signer_seeds]),
            ctx.accounts.from.amount,
        )?;

        token::close_account(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::CloseAccount {
                    account: ctx.accounts.from.to_account_info(),
                    destination: ctx.accounts.payer.to_account_info(),
                    authority: ctx.accounts.master_token_owner.to_account_info(),
                },
            )
            .with_signer(&[&recipe_signer_seeds]),
        )?;

        Ok(())
    }
}

#[derive(Accounts)]
#[instruction(ingredients: String, roots: Vec<[u8; 32]>)]
pub struct CreateRecipe<'info> {
    #[account(
        init,
        payer = payer,
        space =
          8                         // discriminator
        + 32                        // Pubkey
        + 4 + MAX_URI_LENGTH        // String
        + 4 + roots.len() * 32      // Vec
    )]
    pub recipe: Account<'info, Recipe>,

    /// CHECK: Checked in program
    pub authority: AccountInfo<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,

    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct StartDish<'info> {
    pub recipe: Account<'info, Recipe>,

    #[account(
        init,
        seeds = [
            PREFIX,
            recipe.key().to_bytes().as_ref(),
            payer.key().to_bytes().as_ref()
        ],
        bump,
        payer = payer,
        space = 8       // discriminator
            + 32        // authority
            + 32        // recipe
            + 8         // ingredients_added
            + 1         // completed
            ,
    )]
    pub dish: Account<'info, Dish>,

    #[account(mut)]
    pub payer: Signer<'info>,

    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct AddIngredient<'info> {
    pub recipe: Account<'info, Recipe>,

    #[account(mut)]
    pub dish: Account<'info, Dish>,

    pub ingredient_mint: Account<'info, token::Mint>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub ingredient_store: AccountInfo<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,

    #[account(mut)]
    pub from: Account<'info, token::TokenAccount>,

    pub system_program: Program<'info, System>,

    pub token_program: Program<'info, token::Token>,

    pub rent: Sysvar<'info, Rent>,
}

#[derive(Accounts)]
pub struct RemoveIngredient<'info> {
    #[account(mut)]
    pub dish: Account<'info, Dish>,

    pub ingredient_mint: Account<'info, token::Mint>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub ingredient_store: AccountInfo<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,

    #[account(mut)]
    pub to: Account<'info, token::TokenAccount>,

    pub system_program: Program<'info, System>,

    pub token_program: Program<'info, token::Token>,

    pub rent: Sysvar<'info, Rent>,
}

#[derive(Accounts)]
pub struct MakeDish<'info> {
    pub recipe: Account<'info, Recipe>,

    #[account(mut)]
    pub dish: Account<'info, Dish>,

    #[account(mut)]
    pub payer: Signer<'info>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub metadata_new_metadata: AccountInfo<'info>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub metadata_new_edition: AccountInfo<'info>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub metadata_master_edition: AccountInfo<'info>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub metadata_new_mint: AccountInfo<'info>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub metadata_edition_mark_pda: AccountInfo<'info>,

    pub metadata_new_mint_authority: Signer<'info>,

    // PDA of recipe and master mint
    /// CHECK: Checked in program
    pub metadata_master_token_owner: AccountInfo<'info>,

    /// CHECK: Checked in program
    pub metadata_master_token_account: AccountInfo<'info>,

    #[account(address = recipe.authority)]
    /// CHECK: Checked in program
    pub metadata_new_update_authority: AccountInfo<'info>,

    /// CHECK: Checked in program
    pub metadata_master_metadata: AccountInfo<'info>,

    /// CHECK: Checked in program
    pub metadata_master_mint: AccountInfo<'info>,

    pub system_program: Program<'info, System>,

    pub token_program: Program<'info, token::Token>,

    #[account(address = mpl_token_metadata::id())]
    /// CHECK: Checked in program
    pub token_metadata_program: AccountInfo<'info>,

    pub rent: Sysvar<'info, Rent>,
}

#[derive(Accounts)]
pub struct ConsumeIngredient<'info> {
    pub recipe: Account<'info, Recipe>,

    #[account(mut)]
    pub dish: Account<'info, Dish>,

    // supply changes
    #[account(mut)]

    pub ingredient_mint: Account<'info, token::Mint>,

    #[account(mut)]
    /// CHECK: Checked in program
    pub ingredient_store: AccountInfo<'info>,

    #[account(mut)]
    pub payer: Signer<'info>,

    pub system_program: Program<'info, System>,

    pub token_program: Program<'info, token::Token>,
}

#[derive(Accounts)]
pub struct ReclaimMasterEdition<'info> {
    pub recipe: Account<'info, Recipe>,

    /// CHECK: Checked in program
    pub master_mint: AccountInfo<'info>,

    // PDA of recipe and master mint
    /// CHECK: Checked in program
    pub master_token_owner: AccountInfo<'info>,

    #[account(mut)]
    pub from: Account<'info, token::TokenAccount>,

    #[account(mut)]
    pub to: Account<'info, token::TokenAccount>,

    #[account(mut)]
    pub payer: Signer<'info>,

    pub system_program: Program<'info, System>,

    pub token_program: Program<'info, token::Token>,
}

#[account]
#[derive(Default)]
pub struct Recipe {
    pub authority: Pubkey,
    pub ingredients: String,
    pub roots: Vec<[u8; 32]>,
}

#[account]
#[derive(Default)]
pub struct Dish {
    pub authority: Pubkey,
    // redundant since pda. kept for matching
    pub recipe: Pubkey,
    pub ingredients_added: u64,
    pub completed: bool,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Invalid Merkle proof")]
    InvalidProof,
    #[msg("Invalid Mint")]
    InvalidMint,
    #[msg("Invalid Mint PDA")]
    InvalidMintPDA,
    #[msg("Mismatched Recipe")]
    MismatchedRecipe,
    #[msg("Incomplete Recipe")]
    IncompleteRecipe,
    #[msg("Recipe Already Completed")]
    RecipeAlreadyCompleted,
    #[msg("Recipe Not Completed")]
    RecipeNotCompleted,
    #[msg("Invalid Authority")]
    InvalidAuthority,
    #[msg("Arithmetic Overflow")]
    ArithmeticOverflow,
    #[msg("Mismatched Edition Mint Parent")]
    MismatchedEditionMint,
    #[msg("Edition Zero Invalid")]
    EditionZeroInvalid,
    #[msg("Derived Key Invalid")]
    DerivedKeyInvalid,
}



