fireball/program/tests/smoke.rs
===============================

Last edited: 2022-04-29 15:13:47

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]

use anchor_lang::{InstructionData, ToAccountMetas};
use solana_program_test::*;
use solana_sdk::{
    instruction::{Instruction},
    native_token::LAMPORTS_PER_SOL,
    program_pack::Pack,
    pubkey::Pubkey,
    signature::Signer,
    signer::keypair::Keypair,
    system_instruction,
    system_program,
    transaction::Transaction,
};

fn merkle_layer(
    layer: &[solana_program::keccak::Hash],
) -> Vec<solana_program::keccak::Hash> {
    let mut next_layer = Vec::new();
    for i in 0..layer.len() {
        if i % 2 == 0 {
            if i + 1 < layer.len() {
                let lhs = &layer[i].0;
                let rhs = &layer[i+1].0;
                if lhs <= rhs {
                    next_layer.push(solana_program::keccak::hashv(&[&[0x01], lhs, rhs]));
                } else {
                    next_layer.push(solana_program::keccak::hashv(&[&[0x01], rhs, lhs]));
                }
            } else {
                next_layer.push(layer[i]);
            }
        }
    }
    next_layer
}

fn merkle_root(
    leafs: &[solana_program::keccak::Hash],
) -> solana_program::keccak::Hash {
    let mut layer = leafs.to_vec();
    loop {
        if layer.len() <= 1 { return layer[0]; }
        layer = merkle_layer(&layer);
    }
}

// TODO: dedup
fn merkle_proof(
    leafs: &[solana_program::keccak::Hash],
    mut index: usize,
) -> Vec<solana_program::keccak::Hash> {
    let mut proof = Vec::new();
    let mut layer = leafs.to_vec();
    loop {
        let sibling = index ^ 1;
        if sibling < layer.len() {
            proof.push(layer[sibling]);
        }
        index = index / 2;
        if layer.len() <= 1 { return proof; }
        layer = merkle_layer(&layer);
    }
}

async fn nft_setup_transaction(
    payer: &dyn Signer,
    mint: &dyn Signer,
    recent_blockhash: &solana_sdk::hash::Hash,
    rent: &solana_sdk::sysvar::rent::Rent,
) -> Result<Transaction, Box<dyn std::error::Error>> {
    let (metadata_key, _metadata_bump) = mpl_token_metadata::pda::find_metadata_account(&mint.pubkey());
    let (edition_key, _edition_bump) = mpl_token_metadata::pda::find_master_edition_account(&mint.pubkey());

    let payer_pubkey = payer.pubkey();
    let instructions = vec![
            system_instruction::create_account(
                &payer.pubkey(),
                &mint.pubkey(),
                rent.minimum_balance(spl_token::state::Mint::LEN),
                spl_token::state::Mint::LEN as u64,
                &spl_token::id(),
            ),
            spl_token::instruction::initialize_mint(
                &spl_token::id(),
                &mint.pubkey(),
                &payer.pubkey(), // mint auth
                Some(&payer_pubkey), // freeze auth
                0,
            )?,
            spl_associated_token_account::create_associated_token_account(
                &payer.pubkey(), // funding
                &payer.pubkey(), // wallet to create for
                &mint.pubkey(),
            ),
            spl_token::instruction::mint_to(
                &spl_token::id(),
                &mint.pubkey(),
                &spl_associated_token_account::get_associated_token_address(
                    &payer.pubkey(),
                    &mint.pubkey(),
                ),
                &payer.pubkey(),
                &[],
                1
            )?,
            mpl_token_metadata::instruction::create_metadata_accounts(
                mpl_token_metadata::id(),
                metadata_key,
                mint.pubkey(),
                payer.pubkey(), // mint auth
                payer.pubkey(), // payer
                payer.pubkey(), // update auth
                "test".to_string(), // name
                "".to_string(), // symbol
                "".to_string(), // uri
                Some(vec![mpl_token_metadata::state::Creator{
                    address: payer.pubkey(),
                    verified: true,
                    share: 100,
                }]),
                0, // seller_fee_basis_points
                true, // update_auth_is_signer
                true, // is_mutable
            ),
            mpl_token_metadata::instruction::create_master_edition(
                mpl_token_metadata::id(),
                edition_key,
                mint.pubkey(),
                payer.pubkey(), // update auth
                payer.pubkey(), // mint auth
                metadata_key,
                payer.pubkey(), // payer
                None, // limited edition supply
            ),
        ];

    Ok(Transaction::new_signed_with_payer(
        &instructions,
        Some(&payer.pubkey()),
        &[payer, mint],
        *recent_blockhash,
    ))
}

#[tokio::test]
async fn test_make_dish() {

    let mut pc = ProgramTest::default();

    pc.add_program("mpl_fireball", mpl_fireball::id(), None);
    pc.add_program("mpl_token_metadata", mpl_token_metadata::id(), None);

    let (mut banks_client, payer, recent_blockhash) = pc.start().await;

    let rent = banks_client.get_rent().await.unwrap();

    let recipe_ingredients = [
        Keypair::new(),
        Keypair::new(),
        Keypair::new(),
        Keypair::new(),
    ];

    let leafs = recipe_ingredients
        .iter()
        .map(|kp|
            solana_program::keccak::hashv(&[
                &[0x00],
                kp.pubkey().as_ref(),
            ])
        )
        .collect::<Vec<_>>();

    let alice = Keypair::new();

    banks_client.process_transaction(
        Transaction::new_signed_with_payer(
            &[system_instruction::transfer(
                &payer.pubkey(),
                &alice.pubkey(),
                LAMPORTS_PER_SOL,
            )],
            Some(&payer.pubkey()),
            &[&payer],
            recent_blockhash,
        )
    ).await.unwrap();

    // build the ingredient NFTs
    for kp in &recipe_ingredients {
        banks_client.process_transaction(
            nft_setup_transaction(&alice, kp, &recent_blockhash, &rent).await.unwrap()
        ).await.unwrap();
    }

    // make the new nft
    let master_mint = Keypair::new();
    let (master_metadata_key, _) = mpl_token_metadata::pda::find_metadata_account(&master_mint.pubkey());
    let (master_edition_key, _) = mpl_token_metadata::pda::find_master_edition_account(&master_mint.pubkey());
    banks_client.process_transaction(
        nft_setup_transaction(&payer, &master_mint, &recent_blockhash, &rent).await.unwrap()
    ).await.unwrap();

    let recipe = Keypair::new();
    let (recipe_owner, recipe_signer_bump) = Pubkey::find_program_address(
      &[
        mpl_fireball::PREFIX,
        recipe.pubkey().as_ref(),
      ],
      &mpl_fireball::id(),
    );

    let recipe_ata = spl_associated_token_account::get_associated_token_address(
        &recipe_owner,
        &master_mint.pubkey(),
    );

    let root = merkle_root(&leafs);
    banks_client.process_transaction(
        Transaction::new_signed_with_payer(
            &[
                Instruction {
                    program_id: mpl_fireball::id(),
                    accounts: mpl_fireball::accounts::CreateRecipe {
                        recipe: recipe.pubkey(),
                        authority: payer.pubkey(),
                        payer: payer.pubkey(),
                        system_program: system_program::id(),
                    }.to_account_metas(None),
                    data: mpl_fireball::instruction::CreateRecipes {
                        ingredients: "".to_string(),
                        roots: vec![root.0],
                    }.data(),
                },
                spl_associated_token_account::create_associated_token_account(
                    &payer.pubkey(), // funding
                    &recipe_owner, // wallet to create for
                    &master_mint.pubkey(),
                ),
                spl_token::instruction::transfer(
                    &spl_token::id(),
                    &spl_associated_token_account::get_associated_token_address(
                        &payer.pubkey(),
                        &master_mint.pubkey(),
                    ),
                    &recipe_ata,
                    &payer.pubkey(),
                    &[],
                    1
                ).unwrap(),
            ],
            Some(&payer.pubkey()),
            &[&payer, &recipe],
            recent_blockhash,
        )
    ).await.unwrap();


    let (dish_key, dish_bump) = Pubkey::find_program_address(
        &[
            mpl_fireball::PREFIX,
            recipe.pubkey().as_ref(),
            alice.pubkey().as_ref(),
        ],
        &mpl_fireball::id(),
    );

    banks_client.process_transaction(
        Transaction::new_signed_with_payer(
            &[Instruction {
                program_id: mpl_fireball::id(),
                accounts: mpl_fireball::accounts::StartDish {
                    recipe: recipe.pubkey(),
                    dish: dish_key,
                    payer: alice.pubkey(),
                    system_program: system_program::id(),
                }.to_account_metas(None),
                data: mpl_fireball::instruction::StartDish {
                    _dish_bump: dish_bump,
                }.data(),
            }],
            Some(&alice.pubkey()),
            &[&alice],
            recent_blockhash,
        )
    ).await.unwrap();

    for (index, ingredient) in recipe_ingredients.iter().enumerate() {
        let proof = merkle_proof(&leafs, index);
        let proof_raw = proof.iter().map(|v| v.0).collect::<Vec<_>>();
        assert!(mpl_fireball::merkle_proof::verify(proof_raw.clone(), root.0, leafs[index].0));
        let ingredient_num = 0u64;
        let (ingredient_key, ingredient_bump) = Pubkey::find_program_address(
            &[
                mpl_fireball::PREFIX,
                dish_key.as_ref(),
                ingredient_num.to_le_bytes().as_ref(),
            ],
            &mpl_fireball::id(),
        );

        let new_mint = Keypair::new();
        let (new_metadata_key, _) = mpl_token_metadata::pda::find_metadata_account(&new_mint.pubkey());
        let (new_edition_key, _) = mpl_token_metadata::pda::find_master_edition_account(&new_mint.pubkey());

        let edition = index as u64;
        let as_string = edition.checked_div(mpl_token_metadata::state::EDITION_MARKER_BIT_SIZE).unwrap().to_string();
        let (new_edition_mark_key, _) = mpl_token_metadata::pda::find_edition_account(
            &master_mint.pubkey(), as_string); // WTF?

        let fulfill_instructions = [
            Instruction {
                program_id: mpl_fireball::id(),
                accounts: mpl_fireball::accounts::AddIngredient {
                    recipe: recipe.pubkey(),
                    dish: dish_key,
                    ingredient_mint: ingredient.pubkey(),
                    ingredient_store: ingredient_key,
                    payer: alice.pubkey(),
                    from: spl_associated_token_account::get_associated_token_address(
                        &alice.pubkey(),
                        &ingredient.pubkey(),
                    ),
                    system_program: system_program::id(),
                    token_program: spl_token::id(),
                    rent: solana_program::sysvar::rent::id(),
                }.to_account_metas(None),
                data: mpl_fireball::instruction::AddIngredient {
                    ingredient_bump,
                    ingredient_num,
                    proof: proof_raw,
                }.data(),
            },
            system_instruction::create_account(
                &alice.pubkey(),
                &new_mint.pubkey(),
                rent.minimum_balance(spl_token::state::Mint::LEN),
                spl_token::state::Mint::LEN as u64,
                &spl_token::id(),
            ),
            spl_token::instruction::initialize_mint(
                &spl_token::id(),
                &new_mint.pubkey(),
                &alice.pubkey(), // mint auth
                Some(&alice.pubkey()), // freeze auth
                0,
            ).unwrap(),
            spl_associated_token_account::create_associated_token_account(
                &alice.pubkey(), // funding
                &alice.pubkey(), // wallet to create for
                &new_mint.pubkey(),
            ),
            spl_token::instruction::mint_to(
                &spl_token::id(),
                &new_mint.pubkey(),
                &spl_associated_token_account::get_associated_token_address(
                    &alice.pubkey(),
                    &new_mint.pubkey(),
                ),
                &alice.pubkey(),
                &[],
                1
            ).unwrap(),
            Instruction {
                program_id: mpl_fireball::id(),
                accounts: mpl_fireball::accounts::MakeDish {
                    recipe: recipe.pubkey(),
                    dish: dish_key,
                    payer: alice.pubkey(),
                    metadata_new_metadata: new_metadata_key,
                    metadata_new_edition: new_edition_key,
                    metadata_master_edition: master_edition_key,
                    metadata_new_mint: new_mint.pubkey(),
                    metadata_edition_mark_pda: new_edition_mark_key,
                    metadata_new_mint_authority: alice.pubkey(),
                    metadata_master_token_owner: recipe_owner,
                    metadata_master_token_account: recipe_ata,
                    metadata_new_update_authority: payer.pubkey(), // recipe authority
                    metadata_master_metadata: master_metadata_key,
                    metadata_master_mint: master_mint.pubkey(),
                    system_program: system_program::id(),
                    token_program: spl_token::id(),
                    token_metadata_program: mpl_token_metadata::id(),
                    rent: solana_program::sysvar::rent::id(),
                }.to_account_metas(None),
                data: mpl_fireball::instruction::MakeDish {
                    recipe_signer_bump,
                    edition,
                }.data(),
            },
        ];

        banks_client.process_transaction(
            Transaction::new_signed_with_payer(
                &fulfill_instructions,
                Some(&alice.pubkey()),
                &[&alice, &new_mint],
                recent_blockhash,
            )
        ).await.unwrap();

        let close_instructions = [
            Instruction {
                program_id: mpl_fireball::id(),
                accounts: mpl_fireball::accounts::ConsumeIngredient {
                    recipe: recipe.pubkey(),
                    dish: dish_key,
                    ingredient_mint: ingredient.pubkey(),
                    ingredient_store: ingredient_key,
                    payer: alice.pubkey(),
                    system_program: system_program::id(),
                    token_program: spl_token::id(),
                }.to_account_metas(None),
                data: mpl_fireball::instruction::ConsumeIngredient {
                    ingredient_bump,
                    ingredient_num,
                }.data(),
            },
        ];

        banks_client.process_transaction(
            Transaction::new_signed_with_payer(
                &close_instructions,
                Some(&alice.pubkey()),
                &[&alice],
                recent_blockhash,
            )
        ).await.unwrap();
    }
}


