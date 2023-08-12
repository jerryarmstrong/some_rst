program/tests/initialize.rs
===========================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    // #![cfg(feature = "test-bpf")]
// pub mod utils;

// use mpl_migration_validator::{instruction::InitializeArgs, state::UnlockMethod};
// use num_traits::FromPrimitive;
// use solana_program_test::{tokio, BanksClientError};
// use solana_sdk::{
//     instruction::InstructionError, signature::Keypair, signer::Signer,
//     transaction::TransactionError,
// };
// use utils::*;

// #[tokio::test]
// async fn initialize_successfully() {
//     let mut context = setup_context().await;

//     // Create a default NFT to use as a collection.
//     let mut nft = NfTest::new();
//     nft.mint_default(&mut context, None).await.unwrap();

//     // Create our migration state manager.
//     let mut migratorr = Migratorr::new(nft.mint_pubkey());

//     // Set up our initialize args
//     let unlock_method = UnlockMethod::Timed;

//     let args = InitializeArgs {
//         rule_set: None, // this defaults to the default public key
//         unlock_method,
//         collection_size: 0,
//     };

//     let payer = context.payer.dirty_clone();

//     // Initialize the migration state account on-chain
//     migratorr
//         .initialize(&mut context, &payer, &payer, &nft, args)
//         .await
//         .unwrap();

//     // Refresh the migratorr's state from the on-chain account.
//     migratorr.refresh_state(&mut context).await.unwrap();

//     assert_eq!(migratorr.mint(), nft.mint_pubkey());
//     assert_eq!(migratorr.authority(), payer.pubkey());
// }

// #[tokio::test]
// async fn cannot_initialize_twice() {
//     let mut context = setup_context().await;

//     // Create a default NFT to use as a collection.
//     let mut nft = NfTest::new();
//     nft.mint_default(&mut context, None).await.unwrap();

//     // Create our migration state manager.
//     let migratorr = Migratorr::new(nft.mint_pubkey());

//     // Set up our initialize args
//     let unlock_method = UnlockMethod::Timed;

//     let args = InitializeArgs {
//         rule_set: None, // this defaults to the default public key
//         unlock_method,
//         collection_size: 0,
//     };

//     let payer = context.payer.dirty_clone();

//     // Initialize the migration state account on-chain
//     migratorr
//         .initialize(&mut context, &payer, &payer, &nft, args.clone())
//         .await
//         .unwrap();

//     context.warp_to_slot(100).unwrap();

//     let err = migratorr
//         .initialize(&mut context, &payer, &payer, &nft, args)
//         .await
//         .unwrap_err();

//     // The account allocation call to the system program will fail with
//     // a custom error of 0 if the account already exists.
//     assert_custom_error_ix!(0, err, 0);
// }

// #[tokio::test]
// async fn init_migration_separate_authority() {
//     let mut context = setup_context().await;

//     // Create an authority that is separate from the payer.
//     let authority = Keypair::new();
//     authority
//         .airdrop(&mut context, 1_000_000_000)
//         .await
//         .unwrap();

//     // Create a default NFT to use as a collection.
//     let mut nft = NfTest::new();
//     nft.mint_default(&mut context, Some(authority.dirty_clone()))
//         .await
//         .unwrap();

//     // Create our migration state manager.
//     let mut migratorr = Migratorr::new(nft.mint_pubkey());

//     // Set up our initialize args
//     let unlock_method = UnlockMethod::Timed;

//     let args = InitializeArgs {
//         rule_set: None, // this defaults to the default public key
//         unlock_method,
//         collection_size: 0,
//     };

//     let payer = context.payer.dirty_clone();

//     // Initialize the migration state account on-chain
//     migratorr
//         .initialize(&mut context, &payer, &authority, &nft, args)
//         .await
//         .unwrap();

//     // Refresh the migratorr's state from the on-chain account.
//     migratorr.refresh_state(&mut context).await.unwrap();

//     assert_eq!(migratorr.mint(), nft.mint_pubkey());
//     assert_eq!(migratorr.authority(), authority.pubkey());
// }


