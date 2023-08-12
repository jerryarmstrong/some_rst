program/tests/update.rs
=======================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]
pub mod utils;

use mpl_migration_validator::{
    self,
    errors::MigrationError,
    instruction::{InitializeArgs, UpdateArgs},
    state::UnlockMethod,
};
use num_traits::FromPrimitive;
use solana_program::{native_token::LAMPORTS_PER_SOL, pubkey::Pubkey};
use solana_program_test::{tokio, BanksClientError};
use solana_sdk::{
    instruction::InstructionError, signature::Keypair, signer::Signer,
    transaction::TransactionError,
};

use crate::utils::*;

#[tokio::test]
async fn update_rule_set() {
    let mut context = setup_context().await;

    // Create an authority that is separate from the payer.
    let authority = Keypair::new();
    authority
        .airdrop(&mut context, 1_000_000_000)
        .await
        .unwrap();

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, Some(authority.dirty_clone()))
        .await
        .unwrap();

    // Create our migration state manager.
    let mut migratorr = Migratorr::new(nft.mint_pubkey());

    // Set up our initialize args
    let unlock_method = UnlockMethod::Timed;

    let args = InitializeArgs {
        rule_set: None, // this defaults to the default public key
        unlock_method,
        collection_size: 0,
    };

    let payer = context.payer.dirty_clone();

    // Initialize the migration state account on-chain
    migratorr
        .initialize(&mut context, &payer, &authority, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), authority.pubkey());

    let dummy_rule_set = Pubkey::new_unique();
    let update_args = UpdateArgs {
        rule_set: Some(dummy_rule_set),
        collection_size: None,
        new_update_authority: None,
    };

    migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap();

    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.rule_set(), dummy_rule_set);
}

#[tokio::test]
async fn update_collection_size() {
    let mut context = setup_context().await;

    // Create an authority that is separate from the payer.
    let authority = Keypair::new();
    authority
        .airdrop(&mut context, 1_000_000_000)
        .await
        .unwrap();

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, Some(authority.dirty_clone()))
        .await
        .unwrap();

    // Create our migration state manager.
    let mut migratorr = Migratorr::new(nft.mint_pubkey());

    // Set up our initialize args
    let unlock_method = UnlockMethod::Timed;

    let args = InitializeArgs {
        rule_set: None, // this defaults to the default public key
        unlock_method,
        collection_size: 0,
    };

    let payer = context.payer.dirty_clone();

    // Initialize the migration state account on-chain
    migratorr
        .initialize(&mut context, &payer, &authority, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), authority.pubkey());

    let new_collection_size = 888;
    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: Some(new_collection_size),
        new_update_authority: None,
    };

    migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap();

    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.collection_size(), new_collection_size);
}

#[tokio::test]
async fn update_authority() {
    let mut context = setup_context().await;

    // Create an authority that is separate from the payer.
    let authority = Keypair::new();
    authority
        .airdrop(&mut context, 1_000_000_000)
        .await
        .unwrap();

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, Some(authority.dirty_clone()))
        .await
        .unwrap();

    // Create our migration state manager.
    let mut migratorr = Migratorr::new(nft.mint_pubkey());

    // Set up our initialize args
    let unlock_method = UnlockMethod::Timed;

    let args = InitializeArgs {
        rule_set: None, // this defaults to the default public key
        unlock_method,
        collection_size: 0,
    };

    let payer = context.payer.dirty_clone();

    // Initialize the migration state account on-chain
    migratorr
        .initialize(&mut context, &payer, &authority, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), authority.pubkey());

    let new_authority = Pubkey::new_unique();

    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: None,
        new_update_authority: Some(new_authority),
    };

    migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap();

    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.authority(), new_authority);
}

#[tokio::test]
async fn update_after_items_migrated() {
    let mut context = setup_context().await;

    // Create an authority that is separate from the payer.
    let authority = Keypair::new();
    let authority_pubkey = authority.pubkey();

    authority
        .airdrop(&mut context, 1_000_000_000)
        .await
        .unwrap();

    // Create a default NFT to use as a collection.
    let mut collection_nft = NfTest::new();
    collection_nft
        .mint_default(&mut context, Some(authority.dirty_clone()))
        .await
        .unwrap();

    // Create an item NFT and add it to our collection.
    let mut item_nft = NfTest::new();
    item_nft
        .mint_default(&mut context, Some(authority.dirty_clone()))
        .await
        .unwrap();

    item_nft
        .set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: authority.dirty_clone(),
                nft_update_authority: authority_pubkey,
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

    let payer = context.payer.dirty_clone();

    // Create our migration state manager.
    let mut migratorr = Migratorr::new(collection_nft.mint_pubkey());
    migratorr.init_signer(&mut context, &payer).await.unwrap();

    // Set up our initialize args
    let unlock_method = UnlockMethod::Timed;

    let args = InitializeArgs {
        rule_set: None, // this defaults to the default public key
        unlock_method,
        collection_size: 1,
    };

    // Initialize the migration state account on-chain
    migratorr
        .initialize(&mut context, &payer, &authority, &collection_nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), collection_nft.mint_pubkey());
    assert_eq!(migratorr.authority(), authority.pubkey());

    println!("migration state: {:?}", migratorr.state());
    println!("migration pubkey: {:?}", migratorr.pubkey());

    // Inject timestamp state to allow the migration to be unlocked.
    migratorr.unlock_collection(&mut context, &authority).await;

    // Enable migration.
    migratorr
        .start(&mut context, &payer, &authority, &collection_nft)
        .await
        .unwrap();

    // These all should still work because no items have been migrated yet.
    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: Some(2),
        new_update_authority: None,
    };

    migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap();

    let new_authority = Keypair::new();
    new_authority
        .airdrop(&mut context, LAMPORTS_PER_SOL)
        .await
        .unwrap();

    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: None,
        new_update_authority: Some(new_authority.pubkey()),
    };

    migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap();

    warp100(&mut context).await;
    warp100(&mut context).await;

    // Switch authority back
    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: None,
        new_update_authority: Some(authority.pubkey()),
    };

    migratorr
        .update(&mut context, &new_authority, update_args)
        .await
        .unwrap();

    // Migrate the item.
    migratorr
        .migrate_item(
            &mut context,
            &payer,
            collection_nft.mint_pubkey(),
            authority.pubkey(),
            &item_nft,
        )
        .await
        .unwrap();

    // This will now fail because migrated items > 0.
    let dummy_rule_set = Pubkey::new_unique();
    let update_args = UpdateArgs {
        rule_set: Some(dummy_rule_set),
        collection_size: None,
        new_update_authority: None,
    };

    let err = migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap_err();

    assert_custom_error_ix!(0, err, MigrationError::MigrationInProgress);

    // This will now fail because migrated items > 0.
    let dummy_new_authority = Pubkey::new_unique();
    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: None,
        new_update_authority: Some(dummy_new_authority),
    };

    let err = migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap_err();

    assert_custom_error_ix!(0, err, MigrationError::MigrationInProgress);

    // This will still succeed.
    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: Some(2),
        new_update_authority: None,
    };

    migratorr
        .update(&mut context, &authority, update_args)
        .await
        .unwrap();

    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.collection_size(), 2);
}


