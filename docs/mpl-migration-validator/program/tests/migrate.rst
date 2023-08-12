program/tests/migrate.rs
========================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]
pub mod utils;

use mpl_migration_validator::{instruction::InitializeArgs, state::UnlockMethod, PROGRAM_SIGNER};
use mpl_token_metadata::{
    pda::find_collection_authority_account,
    state::{CollectionAuthorityRecord, TokenDelegateRole, TokenMetadataAccount, TokenState},
};
use num_traits::FromPrimitive;
use solana_program::native_token::LAMPORTS_PER_SOL;
use solana_program_test::{tokio, BanksClientError};
use solana_sdk::{
    instruction::InstructionError, signature::Keypair, signer::Signer,
    transaction::TransactionError,
};

use utils::*;

mod eligible_scenarios {
    use super::*;

    #[tokio::test]
    async fn migrate_collection_success() {
        // The happy path for migrating a collection.
        // No SPL token delegates and tokens start unfrozen.
        //
        // Success States:
        // Token Standard:       ProgrammableNonFungible
        // Token Freeze State:   Frozen
        // TokenRecord Delegate: None
        // TokenRecord Role:     None
        // TokenRecord State:    Unlocked
        let mut context = setup_pnft_context().await;

        let collection_authority = context.payer.dirty_clone();
        let collection_authority_pubkey = collection_authority.pubkey();

        // We create a collection with three NFTs in it.
        let mut collection_nft = NfTest::new();
        collection_nft
            .mint_default(&mut context, None)
            .await
            .unwrap();

        let mut nft1 = NfTest::new();
        nft1.mint_default(&mut context, None).await.unwrap();
        nft1.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority.pubkey(),
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let mut nft2 = NfTest::new();
        nft2.mint_default(&mut context, None).await.unwrap();
        nft2.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority_pubkey,
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let mut nft3 = NfTest::new();
        nft3.mint_default(&mut context, None).await.unwrap();
        nft3.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority_pubkey,
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let payer = context.payer.dirty_clone();

        // Create default rule set to apply to migrated NFTs.
        let (rule_set, _auth_rules) = create_default_metaplex_rule_set(&mut context, payer).await;

        // Create our migration state manager.
        let mut migratorr = Migratorr::new(collection_nft.mint_pubkey());

        let payer = context.payer.dirty_clone();

        // Initialize the program signer
        migratorr.init_signer(&mut context, &payer).await.unwrap();

        let args = InitializeArgs {
            rule_set: Some(rule_set),
            unlock_method: UnlockMethod::Timed,
            collection_size: 3,
        };

        // Initialize the migration state account on-chain
        migratorr
            .initialize(&mut context, &payer, &payer, &collection_nft, args)
            .await
            .unwrap();

        // Artificially update the timestamp to allow the migration to start
        // and call update to unlock the collection.
        migratorr
            .unlock_collection(&mut context, &collection_authority)
            .await;

        // Now we try to start the migration expecting it to succeed.
        migratorr
            .start(&mut context, &payer, &payer, &collection_nft)
            .await
            .unwrap();

        // Refresh the migratorr's state from the on-chain account.
        migratorr.refresh_state(&mut context).await.unwrap();

        // Check values are as expected.
        assert!(migratorr.state().status.in_progress);
        assert!(!migratorr.state().status.is_locked);
        assert_eq!(migratorr.rule_set(), rule_set);

        // Ensure the collection delegate was created.
        let (delegate_record_pda, bump) =
            find_collection_authority_account(&migratorr.mint(), &PROGRAM_SIGNER);

        // This function call panics if the account doesn't exist.
        let delegate_record_account = get_account(&mut context, &delegate_record_pda).await;

        let delegate_record =
            CollectionAuthorityRecord::safe_deserialize(delegate_record_account.data.as_slice())
                .expect("Failed to deserialize delegate record account");

        // Check authority and bump values are as expected.
        assert_eq!(
            delegate_record.update_authority.unwrap(),
            migratorr.authority()
        );
        assert_eq!(delegate_record.bump, bump);
        // Record matches what was stored in the migration state.
        assert_eq!(migratorr.delegate_record(), delegate_record_pda);

        // We are ready to migrate.

        let token_owner = context.payer.pubkey();

        // NFT 1
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                token_owner,
                &nft1,
            )
            .await
            .unwrap();

        // NFT 2
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                token_owner,
                &nft2,
            )
            .await
            .unwrap();

        // NFT 3
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                token_owner,
                &nft3,
            )
            .await
            .unwrap();

        // Migrate the collection NFT at the end.
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                token_owner,
                &collection_nft,
            )
            .await
            .unwrap();

        // The rule set should match.
        // NFTs had no SPL token delegate so their delegate and role should be None.
        // The NFTs should be unlocked because they weren't frozen initially.
        nft1.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            None,
            None,
            TokenState::Unlocked,
        )
        .await
        .unwrap();

        nft2.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            None,
            None,
            TokenState::Unlocked,
        )
        .await
        .unwrap();

        nft3.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            None,
            None,
            TokenState::Unlocked,
        )
        .await
        .unwrap();
    }

    #[tokio::test]
    async fn unfrozen_with_spl_delegate() {
        // Migrate an unfrozen NFT with an SPL token delegate.
        // This should successfully migrate the NFT to a pNFT and create
        // a TokenRecord with a MigrationDelegate.
        // Its state should be Unlocked since it started unfrozen.
        // The NFT token account should be frozen after migration.
        //
        // Success States:
        // Token Standard:       ProgrammableNonFungible
        // Token Freeze State:   Frozen
        // TokenRecord Delegate: SPL Token Delegate
        // TokenRecord Role:     MigrationDelegate
        // TokenRecord State:    Unlocked
        let mut context = setup_pnft_context().await;

        let collection_authority = context.payer.dirty_clone();
        let collection_authority_pubkey = collection_authority.pubkey();

        // We create a collection to contain the NFT.
        let mut collection_nft = NfTest::new();
        collection_nft
            .mint_default(&mut context, None)
            .await
            .unwrap();

        let mut nft = NfTest::new();
        nft.mint_default(&mut context, None).await.unwrap();
        nft.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority_pubkey,
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let payer = context.payer.dirty_clone();

        // Create default rule set to apply to migrated NFTs.
        let (rule_set, _auth_rules) = create_default_metaplex_rule_set(&mut context, payer).await;

        // Create our migration state manager.
        let mut migratorr = Migratorr::new(collection_nft.mint_pubkey());

        let payer = context.payer.dirty_clone();

        // Initialize the program signer
        migratorr.init_signer(&mut context, &payer).await.unwrap();

        let args = InitializeArgs {
            rule_set: Some(rule_set), // this defaults to the default public key
            unlock_method: UnlockMethod::Timed,
            collection_size: 1,
        };

        // Initialize the migration state account on-chain
        migratorr
            .initialize(&mut context, &payer, &payer, &collection_nft, args)
            .await
            .unwrap();

        // Artificially update the timestamp to allow the migration to start
        // and call update to unlock the collection.
        migratorr
            .unlock_collection(&mut context, &collection_authority)
            .await;

        // Enable migration
        migratorr
            .start(&mut context, &payer, &payer, &collection_nft)
            .await
            .unwrap();

        // Assign a spl token delegate to the NFT
        let delegate = Keypair::new();

        nft.spl_delegate(&mut context, &payer, &delegate.pubkey())
            .await
            .unwrap();

        let token_owner = context.payer.pubkey();

        // Migrate the NFT
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                token_owner,
                &nft,
            )
            .await
            .unwrap();

        nft.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            Some(delegate.pubkey()),
            // TODO: refactor to MigrationDelegate once that's enabled in TokenMetadata
            Some(TokenDelegateRole::Migration),
            TokenState::Unlocked,
        )
        .await
        .unwrap();
    }

    #[tokio::test]
    async fn frozen_with_spl_delegate() {
        // Migrate an already frozen NFT with an SPL token delegate.
        // This should successfully migrate the NFT to a pNFT and create
        // a TokenRecord with a MigrationDelegate.
        // Its state should be Locked since it started frozen.
        // The NFT token account should be frozen after migration.
        //
        // Success States:
        // Token Standard:       ProgrammableNonFungible
        // Token Freeze State:   Frozen
        // TokenRecord Delegate: SPL Token Delegate
        // TokenRecord Role:     MigrationDelegate
        // TokenRecord State:    Locked
        let mut context = setup_pnft_context().await;

        let collection_authority = context.payer.dirty_clone();
        let collection_authority_pubkey = collection_authority.pubkey();

        // We create a collection to contain the NFT.
        let mut collection_nft = NfTest::new();
        collection_nft
            .mint_default(&mut context, None)
            .await
            .unwrap();

        let mut nft = NfTest::new();
        nft.mint_default(&mut context, None).await.unwrap();
        nft.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority_pubkey,
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let payer = context.payer.dirty_clone();

        // Create default rule set to apply to migrated NFTs.
        let (rule_set, _auth_rules) = create_default_metaplex_rule_set(&mut context, payer).await;

        // Create our migration state manager.
        let mut migratorr = Migratorr::new(collection_nft.mint_pubkey());

        let payer = context.payer.dirty_clone();

        // Initialize the program signer
        migratorr.init_signer(&mut context, &payer).await.unwrap();

        let args = InitializeArgs {
            rule_set: Some(rule_set), // this defaults to the default public key
            unlock_method: UnlockMethod::Timed,
            collection_size: 1,
        };

        // Initialize the migration state account on-chain
        migratorr
            .initialize(&mut context, &payer, &payer, &collection_nft, args)
            .await
            .unwrap();

        // Artificially update the timestamp to allow the migration to start
        // and call update to unlock the collection.
        migratorr
            .unlock_collection(&mut context, &collection_authority)
            .await;

        // Enable migration
        migratorr
            .start(&mut context, &payer, &payer, &collection_nft)
            .await
            .unwrap();

        // Assign a spl token delegate to the NFT
        let owner = context.payer.dirty_clone();
        let delegate = Keypair::new();
        delegate
            .airdrop(&mut context, LAMPORTS_PER_SOL)
            .await
            .unwrap();

        nft.spl_delegate(&mut context, &payer, &delegate.pubkey())
            .await
            .unwrap();

        nft.refresh_accounts(&mut context).await.unwrap();

        nft.freeze_token(&mut context, &delegate).await.unwrap();

        // Migrate the NFT
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                owner.pubkey(),
                &nft,
            )
            .await
            .unwrap();

        nft.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            Some(delegate.pubkey()),
            Some(TokenDelegateRole::Migration),
            TokenState::Locked,
        )
        .await
        .unwrap();
    }

    #[tokio::test]
    async fn frozen_with_no_spl_delegate() {
        // Migrate an already frozen NFT without an SPL token delegate.
        // This should not be a possible scenario under current delegate and freeze rules
        // but if encountered it can simply be migrated without a delegate and kept frozen.
        // Even though it started frozen, its state should be Unlocked since it has
        // no delegate to unlock it.
        //
        // Success States:
        // Token Standard:       ProgrammableNonFungible
        // Token Freeze State:   Frozen
        // TokenRecord Delegate: None
        // TokenRecord Role:     None
        // TokenRecord State:    Unlocked
        let mut context = setup_pnft_context().await;

        let collection_authority = context.payer.dirty_clone();
        let collection_authority_pubkey = collection_authority.pubkey();

        // We create a collection to contain the NFT.
        let mut collection_nft = NfTest::new();
        collection_nft
            .mint_default(&mut context, None)
            .await
            .unwrap();

        let mut nft = NfTest::new();
        nft.mint_default(&mut context, None).await.unwrap();
        nft.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority_pubkey,
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let payer = context.payer.dirty_clone();

        // Create default rule set to apply to migrated NFTs.
        let (rule_set, _auth_rules) = create_default_metaplex_rule_set(&mut context, payer).await;

        // Create our migration state manager.
        let mut migratorr = Migratorr::new(collection_nft.mint_pubkey());

        let payer = context.payer.dirty_clone();

        // Initialize the program signer
        migratorr.init_signer(&mut context, &payer).await.unwrap();

        let args = InitializeArgs {
            rule_set: Some(rule_set), // this defaults to the default public key
            unlock_method: UnlockMethod::Timed,
            collection_size: 1,
        };

        // Initialize the migration state account on-chain
        migratorr
            .initialize(&mut context, &payer, &payer, &collection_nft, args)
            .await
            .unwrap();

        // Artificially update the timestamp to allow the migration to start
        // and call update to unlock the collection.
        migratorr
            .unlock_collection(&mut context, &collection_authority)
            .await;

        // Enable migration
        migratorr
            .start(&mut context, &payer, &payer, &collection_nft)
            .await
            .unwrap();

        let owner = context.payer.dirty_clone();

        // Simulate a frozen NFT with no delegate by directly injecting the frozen state.
        nft.inject_frozen_state(&mut context).await;

        // Migrate the NFT
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                owner.pubkey(),
                &nft,
            )
            .await
            .unwrap();

        nft.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            None,
            None,
            TokenState::Unlocked,
        )
        .await
        .unwrap();
    }
}

mod ineligible_scenarios {
    use mpl_migration_validator::errors::MigrationError;

    use super::*;

    #[tokio::test]
    async fn only_nonfungible_can_migrate() {
        // Attempt to migrate the following asset types:
        // * Fungible
        // * FungibleAsset
        // * NonFungibleEdition
        // * ProgrammableNonFungible
        // These should all fail.
        let mut context = setup_pnft_context().await;

        let collection_authority = context.payer.dirty_clone();

        // We create a collection to contain the various asset types.
        let mut collection_nft = NfTest::new();
        collection_nft
            .mint_default(&mut context, None)
            .await
            .unwrap();

        let authority = context.payer.dirty_clone();

        // Create NonFungible asset to migrate to a ProgrammableNonFungible
        // to test a second migration and to print an edition from.
        let mut nft = NfTest::new();
        nft.mint_master_with_supply(&mut context, None, 1)
            .await
            .unwrap();
        nft.set_and_verify_collection(
            &mut context,
            SetAndVerifyCollectionArgs {
                collection_metadata: collection_nft.metadata_pubkey(),
                collection_authority: collection_authority.dirty_clone(),
                nft_update_authority: collection_authority.pubkey(),
                collection_mint: collection_nft.mint_pubkey(),
                collection_master_edition_account: collection_nft.edition_pubkey().unwrap(),
                collection_authority_record: None,
            },
        )
        .await
        .unwrap();

        let print_edition = TestPrintEdition::new(&nft, 1);
        print_edition.create(&mut context).await.unwrap();
        print_edition
            .set_and_verify_collection(
                &mut context,
                collection_nft.metadata_pubkey(),
                &collection_authority,
                collection_authority.pubkey(),
                collection_nft.mint_pubkey(),
                collection_nft.edition_pubkey().unwrap(),
                None,
            )
            .await
            .unwrap();

        let fungible = TestAsset::new();
        fungible
            .mint_default_fungible(&mut context, &authority)
            .await
            .unwrap();

        fungible
            .set_and_verify_collection(
                &mut context,
                collection_nft.metadata_pubkey(),
                &collection_authority,
                collection_authority.pubkey(),
                collection_nft.mint_pubkey(),
                collection_nft.edition_pubkey().unwrap(),
                None,
            )
            .await
            .unwrap();

        let fungible_asset = TestAsset::new();
        fungible_asset
            .mint_default_fungible_asset(&mut context, &authority)
            .await
            .unwrap();

        fungible_asset
            .set_and_verify_collection(
                &mut context,
                collection_nft.metadata_pubkey(),
                &collection_authority,
                collection_authority.pubkey(),
                collection_nft.mint_pubkey(),
                collection_nft.edition_pubkey().unwrap(),
                None,
            )
            .await
            .unwrap();

        // Create default rule set to apply to migrated NFTs.
        let (rule_set, _auth_rules) =
            create_default_metaplex_rule_set(&mut context, authority).await;

        // Create our migration state manager.
        let mut migratorr = Migratorr::new(collection_nft.mint_pubkey());

        let payer = context.payer.dirty_clone();

        // Initialize the program signer
        migratorr.init_signer(&mut context, &payer).await.unwrap();

        let args = InitializeArgs {
            rule_set: Some(rule_set), // this defaults to the default public key
            unlock_method: UnlockMethod::Timed,
            collection_size: 1,
        };

        // Initialize the migration state account on-chain
        migratorr
            .initialize(&mut context, &payer, &payer, &collection_nft, args)
            .await
            .unwrap();

        // Artificially update the timestamp to allow the migration to start
        // and call update to unlock the collection.
        migratorr
            .unlock_collection(&mut context, &collection_authority)
            .await;

        // Enable migration
        migratorr
            .start(&mut context, &payer, &payer, &collection_nft)
            .await
            .unwrap();

        // Attempt to migrate the Fungible
        // Error: IncorrectFreezeAuthority
        let err = migratorr
            .migrate_asset(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                payer.pubkey(),
                &fungible,
            )
            .await
            .unwrap_err();

        assert_custom_error_ix!(0, err, MigrationError::IncorrectFreezeAuthority);

        // Attempt to migrate the Fungible Asset
        // Error: IncorrectFreezeAuthority
        let err = migratorr
            .migrate_asset(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                payer.pubkey(),
                &fungible_asset,
            )
            .await
            .unwrap_err();

        assert_custom_error_ix!(0, err, MigrationError::IncorrectFreezeAuthority);

        // Attempt to migrate the Print Edition
        // Error: ImmutableMetadata
        let err = migratorr
            .migrate_print_edition(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                payer.pubkey(),
                &print_edition,
            )
            .await
            .unwrap_err();

        assert_custom_error_ix!(0, err, MigrationError::ImmutableMetadata);

        // Migrate the NonFungible.
        migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                payer.pubkey(),
                &nft,
            )
            .await
            .unwrap();

        // It is now a pNFT, migrating it again should fail.
        // Error: IncorrectTokenStandard
        nft.assert_pnft_migration(
            &mut context,
            Some(rule_set),
            None,
            None,
            TokenState::Unlocked,
        )
        .await
        .unwrap();

        warp100(&mut context).await;

        let err = migratorr
            .migrate_item(
                &mut context,
                &payer,
                collection_nft.mint_pubkey(),
                payer.pubkey(),
                &nft,
            )
            .await
            .unwrap_err();

        assert_custom_error_ix!(0, err, MigrationError::IncorrectTokenStandard);
    }
}


