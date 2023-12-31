programs/trifle/tests/trifle.rs
===============================

Last edited: 2023-07-13 14:48:42

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]

pub mod utils;

use mpl_trifle::instruction::remove_constraint_from_escrow_constraint_model;
use solana_program_test::*;
use solana_sdk::{signer::Signer, transaction::Transaction};
use utils::*;

mod trifle {
    use mpl_trifle::{
        instruction::{transfer_in, transfer_out},
        state::{
            escrow_constraints::EscrowConstraintModel, transfer_effects::TransferEffects,
            trifle::Trifle,
        },
    };
    use solana_program::{borsh::try_from_slice_unchecked, program_pack::Pack};

    use super::*;

    #[tokio::test]
    async fn test_happy_path() {
        let mut context = program_test().start_with_context().await;

        let payer_pubkey = context.payer.pubkey().to_owned();
        let (metadata, master_edition, test_collection) =
            create_nft(&mut context, true, Some(payer_pubkey)).await;
        let test_collection = test_collection.expect("test collection should exist");
        let escrow_constraint_model_addr = create_escrow_constraint_model(
            &mut context,
            TransferEffects::new().with_track(true),
            test_collection,
            vec![metadata.mint.pubkey()],
        )
        .await;

        let (trifle_addr, escrow_addr) = create_trifle(
            &mut context,
            &metadata,
            &master_edition,
            escrow_constraint_model_addr,
            None,
        )
        .await;

        let trifle_account = context
            .banks_client
            .get_account(trifle_addr)
            .await
            .expect("trifle account should exist")
            .expect("trifle account should exist");

        let trifle_account_data: Trifle =
            try_from_slice_unchecked(&trifle_account.data).expect("should deserialize");
        println!("trifle_account: {:#?}", trifle_account_data);
        let constraint_account = context
            .banks_client
            .get_account(escrow_constraint_model_addr)
            .await
            .expect("constraint account should exist")
            .expect("constraint account should exist");
        let constraint_account_data: EscrowConstraintModel =
            try_from_slice_unchecked(&constraint_account.data).expect("should deserialize");
        println!("constraint_account: {:#?}", constraint_account_data);

        // Build the attribute
        let (attribute_metadata, attribute_master_edition, _) =
            create_nft(&mut context, false, None).await;

        let trifle_attribute_token_account =
            spl_associated_token_account::get_associated_token_address(
                &escrow_addr,
                &attribute_metadata.mint.pubkey(),
            );

        let transfer_in_ix = transfer_in(
            mpl_trifle::id(),
            trifle_addr,
            context.payer.pubkey(),
            context.payer.pubkey(),
            escrow_constraint_model_addr,
            escrow_addr,
            Some(metadata.mint.pubkey()),
            Some(metadata.token.pubkey()),
            Some(context.payer.pubkey()),
            attribute_metadata.mint.pubkey(),
            attribute_metadata.token.pubkey(),
            Some(trifle_attribute_token_account),
            Some(attribute_metadata.pubkey),
            Some(attribute_master_edition.pubkey),
            None,
            "test".to_string(),
            1,
        );

        let transfer_in_tx = Transaction::new_signed_with_payer(
            &[transfer_in_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(transfer_in_tx)
            .await
            .expect("transfer in should succeed");

        let trifle_account = context
            .banks_client
            .get_account(trifle_addr)
            .await
            .expect("trifle account should exist")
            .expect("trifle account should exist");

        let trifle_account_data: Trifle =
            try_from_slice_unchecked(&trifle_account.data).expect("should deserialize");
        println!("trifle_account: {:#?}", trifle_account_data);
        let constraint_account = context
            .banks_client
            .get_account(escrow_constraint_model_addr)
            .await
            .expect("constraint account should exist")
            .expect("constraint account should exist");
        let constraint_account_data: EscrowConstraintModel =
            try_from_slice_unchecked(&constraint_account.data).expect("should deserialize");
        println!("constraint_account: {:#?}", constraint_account_data);

        let payer_attribute_token_account =
            spl_associated_token_account::get_associated_token_address(
                &context.payer.pubkey(),
                &attribute_metadata.mint.pubkey(),
            );

        let transfer_out_ix = transfer_out(
            mpl_trifle::id(),
            trifle_addr,
            escrow_constraint_model_addr,
            escrow_addr,
            metadata.token.pubkey(),
            metadata.mint.pubkey(),
            metadata.pubkey,
            None,
            context.payer.pubkey(),
            context.payer.pubkey(),
            attribute_metadata.mint.pubkey(),
            trifle_attribute_token_account,
            payer_attribute_token_account,
            attribute_metadata.pubkey,
            "test".to_string(),
            1,
        );

        let transfer_out_tx = Transaction::new_signed_with_payer(
            &[transfer_out_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(transfer_out_tx)
            .await
            .expect("transfer out should succeed");

        let trifle_account = context
            .banks_client
            .get_account(trifle_addr)
            .await
            .expect("trifle account should exist")
            .expect("trifle account should exist");

        let trifle_account_data: Trifle =
            try_from_slice_unchecked(&trifle_account.data).expect("should deserialize");
        println!("trifle_account: {:#?}", trifle_account_data);

        // right now, the constraint model can be modified even if there are trifle accounts,
        // that reference it, but in the future, we should make it so that the constraint model
        // cannot be modified unless there are no trifles referecing it.

        let remove_constraint_from_model_ix = remove_constraint_from_escrow_constraint_model(
            mpl_trifle::id(),
            escrow_constraint_model_addr,
            context.payer.pubkey(),
            context.payer.pubkey(),
            "test".to_string(),
        );

        let remove_constraint_tx = Transaction::new_signed_with_payer(
            &[remove_constraint_from_model_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(remove_constraint_tx)
            .await
            .expect("remove constraint from model should succeed");

        let constraint_account = context
            .banks_client
            .get_account(escrow_constraint_model_addr)
            .await
            .expect("constraint account should exist")
            .expect("constraint account should exist");
        let constraint_account_data: EscrowConstraintModel =
            try_from_slice_unchecked(&constraint_account.data).expect("should deserialize");
        println!("constraint_account: {:#?}", constraint_account_data);
    }

    #[tokio::test]
    async fn test_transfer_in_with_track_and_burn() {
        let mut context = program_test().start_with_context().await;

        let payer_pubkey = context.payer.pubkey().to_owned();
        let (metadata, master_edition, test_collection) =
            create_nft(&mut context, true, Some(payer_pubkey)).await;
        let test_collection = test_collection.expect("should have a collection");
        let escrow_constraint_model_addr = create_escrow_constraint_model(
            &mut context,
            TransferEffects::new().with_track(true).with_burn(true),
            test_collection,
            vec![metadata.mint.pubkey()],
        )
        .await;

        let (trifle_addr, escrow_addr) = create_trifle(
            &mut context,
            &metadata,
            &master_edition,
            escrow_constraint_model_addr,
            None,
        )
        .await;

        // Build the attribute
        let (attribute_metadata, attribute_master_edition, _) =
            create_nft(&mut context, false, None).await;

        let trifle_attribute_token_account =
            spl_associated_token_account::get_associated_token_address(
                &escrow_addr,
                &attribute_metadata.mint.pubkey(),
            );

        let transfer_in_ix = transfer_in(
            mpl_trifle::id(),
            trifle_addr,
            context.payer.pubkey(),
            context.payer.pubkey(),
            escrow_constraint_model_addr,
            escrow_addr,
            Some(metadata.mint.pubkey()),
            Some(metadata.token.pubkey()),
            Some(master_edition.pubkey),
            attribute_metadata.mint.pubkey(),
            attribute_metadata.token.pubkey(),
            Some(trifle_attribute_token_account),
            Some(attribute_metadata.pubkey),
            Some(attribute_master_edition.pubkey),
            None,
            "test".to_string(),
            1,
        );

        let transfer_in_tx = Transaction::new_signed_with_payer(
            &[transfer_in_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(transfer_in_tx)
            .await
            .expect("transfer in should succeed");
    }

    #[tokio::test]
    async fn test_transfer_in_freeze_parent() {
        let mut context = program_test().start_with_context().await;
        let payer_pubkey = context.payer.pubkey().to_owned();
        let (metadata, master_edition, collection) =
            create_nft(&mut context, true, Some(payer_pubkey)).await;
        let collection = collection.expect("should have a collection");
        let escrow_constraint_model_addr = create_escrow_constraint_model(
            &mut context,
            TransferEffects::new()
                .with_track(true)
                .with_freeze_parent(true),
            collection,
            vec![metadata.mint.pubkey()],
        )
        .await;
        let (trifle, escrow) = create_trifle(
            &mut context,
            &metadata,
            &master_edition,
            escrow_constraint_model_addr,
            None,
        )
        .await;

        // set the trifle program as a delegate of the base NFT's associated token account
        let delegate_ix = spl_token::instruction::approve(
            &spl_token::id(),
            &metadata.token.pubkey(),
            &trifle,
            &context.payer.pubkey(),
            &[&context.payer.pubkey()],
            1,
        )
        .expect("should create delegate instruction");

        let delegate_tx = Transaction::new_signed_with_payer(
            &[delegate_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(delegate_tx)
            .await
            .expect("delegate should succeed");

        let (attribute_metadata, attribute_master_edition, _) =
            create_nft(&mut context, false, None).await;

        let trifle_attribute_token_account =
            spl_associated_token_account::get_associated_token_address(
                &escrow,
                &attribute_metadata.mint.pubkey(),
            );

        let transfer_in_ix = transfer_in(
            mpl_trifle::id(),
            trifle,
            context.payer.pubkey(),
            context.payer.pubkey(),
            escrow_constraint_model_addr,
            escrow,
            Some(metadata.mint.pubkey()),
            Some(metadata.token.pubkey()),
            Some(master_edition.pubkey),
            attribute_metadata.mint.pubkey(),
            attribute_metadata.token.pubkey(),
            Some(trifle_attribute_token_account),
            Some(attribute_metadata.pubkey),
            Some(attribute_master_edition.pubkey),
            None,
            "test".to_string(),
            1,
        );

        let transfer_in_tx = Transaction::new_signed_with_payer(
            &[transfer_in_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(transfer_in_tx)
            .await
            .expect("transfer in should succeed");

        let escrow_token_info = context
            .banks_client
            .get_account(metadata.token.pubkey())
            .await
            .expect("query should succeed")
            .expect("account should be present");

        let escrow_token = spl_token::state::Account::unpack(&escrow_token_info.data).unwrap();
        assert!(escrow_token.is_frozen(), "escrow token should be frozen");

        let payer_attribute_token_account =
            spl_associated_token_account::get_associated_token_address(
                &context.payer.pubkey(),
                &attribute_metadata.mint.pubkey(),
            );

        let transfer_out_ix = transfer_out(
            mpl_trifle::id(),
            trifle,
            escrow_constraint_model_addr,
            escrow,
            metadata.token.pubkey(),
            metadata.mint.pubkey(),
            metadata.pubkey,
            Some(master_edition.pubkey),
            context.payer.pubkey(),
            context.payer.pubkey(),
            attribute_metadata.mint.pubkey(),
            trifle_attribute_token_account,
            payer_attribute_token_account,
            attribute_metadata.pubkey,
            "test".to_string(),
            1,
        );

        let transfer_out_tx = Transaction::new_signed_with_payer(
            &[transfer_out_ix],
            Some(&context.payer.pubkey()),
            &[&context.payer],
            context.last_blockhash,
        );

        context
            .banks_client
            .process_transaction(transfer_out_tx)
            .await
            .expect("transfer out should succeed");

        let escrow_token_info = context
            .banks_client
            .get_account(metadata.token.pubkey())
            .await
            .expect("query should succeed")
            .expect("account should be present");

        let escrow_token = spl_token::state::Account::unpack(&escrow_token_info.data).unwrap();
        assert!(
            !escrow_token.is_frozen(),
            "escrow token should not be frozen"
        );
    }
}


