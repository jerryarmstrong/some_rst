program/tests/close.rs
======================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]
pub mod utils;

use mpl_migration_validator::{
    errors::MigrationError,
    instruction::{InitializeArgs, UpdateArgs},
    state::UnlockMethod,
};
use num_traits::FromPrimitive;
use solana_program_test::{tokio, BanksClientError};
use solana_sdk::{
    instruction::InstructionError, signature::Keypair, signer::Signer,
    transaction::TransactionError,
};
use utils::*;

#[tokio::test]
async fn close_successfully() {
    let mut context = setup_context().await;

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, None).await.unwrap();

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
        .initialize(&mut context, &payer, &payer, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), payer.pubkey());

    migratorr.close(&mut context, &payer).await.unwrap();

    // The account should not exist.
    assert!(context
        .banks_client
        .get_account(migratorr.pubkey())
        .await
        .unwrap()
        .is_none());
}

#[tokio::test]
async fn cannot_close_in_progress_state() {
    let mut context = setup_context().await;

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, None).await.unwrap();

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
        .initialize(&mut context, &payer, &payer, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), payer.pubkey());

    // We need to inject the account with the state set to a timestamp
    // that allows our migration to start.
    let now = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs();
    let mut state = migratorr.state().clone();
    state.status.unlock_time = now as i64 - 2;

    // Set the state on the account.
    migratorr.inject_state(&mut context, state).await;

    // Warp ahead to ensure account is updated.
    context.warp_to_slot(100).unwrap();

    // Update the state account on-chain. This checks the current time
    // and updates the is_unlocked field if the wait time has passed.s
    let update_args = UpdateArgs {
        rule_set: None,
        collection_size: None,
        new_update_authority: None,
    };

    migratorr
        .update(&mut context, &payer, update_args)
        .await
        .unwrap();

    // Now we try to start the migration expecting it to succeed.
    migratorr
        .start(&mut context, &payer, &payer, &nft)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    // Check values are as expected.
    assert!(migratorr.state().status.in_progress);
    assert!(!migratorr.state().status.is_locked);

    // Closing should now fail because the migration is in progress.
    let err = migratorr.close(&mut context, &payer).await.unwrap_err();

    assert_custom_error_ix!(0, err, MigrationError::MigrationInProgress);

    // The account should still exist.
    assert!(context
        .banks_client
        .get_account(migratorr.pubkey())
        .await
        .unwrap()
        .is_some());
}

#[tokio::test]
async fn cannot_close_already_migrated() {
    let mut context = setup_context().await;

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, None).await.unwrap();

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
        .initialize(&mut context, &payer, &payer, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), payer.pubkey());

    // We need to inject the account with the state set to a completed migration.
    let now = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs();
    let mut state = migratorr.state().clone();
    state.status.unlock_time = now as i64 - 2;
    state.status.in_progress = false;
    state.status.is_locked = false;
    state.status.items_migrated = 10;
    state.collection_info.size = 10;

    // Set the state on the account.
    migratorr.inject_state(&mut context, state).await;

    // Warp ahead to ensure account is updated.
    context.warp_to_slot(100).unwrap();

    // Closing should now fail because the migration has completed.
    let err = migratorr.close(&mut context, &payer).await.unwrap_err();

    assert_custom_error_ix!(0, err, MigrationError::MigrationAlreadyCompleted);

    // The account should still exist.
    assert!(context
        .banks_client
        .get_account(migratorr.pubkey())
        .await
        .unwrap()
        .is_some());
}

#[tokio::test]
async fn authority_must_match() {
    // We can only close accounts for which we are the authority.

    let mut context = setup_context().await;

    let incorrect_authority = Keypair::new();
    incorrect_authority
        .airdrop(&mut context, 1_000_000)
        .await
        .unwrap();

    // Create a default NFT to use as a collection.
    let mut nft = NfTest::new();
    nft.mint_default(&mut context, None).await.unwrap();

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
        .initialize(&mut context, &payer, &payer, &nft, args)
        .await
        .unwrap();

    // Refresh the migratorr's state from the on-chain account.
    migratorr.refresh_state(&mut context).await.unwrap();

    assert_eq!(migratorr.mint(), nft.mint_pubkey());
    assert_eq!(migratorr.authority(), payer.pubkey());

    let err = migratorr
        .close(&mut context, &incorrect_authority)
        .await
        .unwrap_err();

    assert_custom_error_ix!(0, err, MigrationError::InvalidAuthority);

    // The account should not exist.
    assert!(context
        .banks_client
        .get_account(migratorr.pubkey())
        .await
        .unwrap()
        .is_some());
}


