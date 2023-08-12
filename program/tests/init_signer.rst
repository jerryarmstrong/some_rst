program/tests/init_signer.rs
============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]
pub mod utils;

use borsh::BorshDeserialize;
use mpl_migration_validator::{errors::MigrationError, instruction::init_signer};
use num_traits::FromPrimitive;
use solana_program_test::{tokio, BanksClientError};
use solana_sdk::{
    instruction::InstructionError,
    signer::Signer,
    transaction::{Transaction, TransactionError},
};

use crate::utils::*;

#[tokio::test]
async fn successfully_init_signer() {
    let mut context = setup_context().await;

    let (program_signer_pubkey, bump) = find_program_signer_pda();

    let instruction = init_signer(context.payer.pubkey());

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&context.payer.pubkey()),
        &[&context.payer],
        context.last_blockhash,
    );

    context
        .banks_client
        .process_transaction(transaction.clone())
        .await
        .unwrap();

    let program_signer_account = context
        .banks_client
        .get_account(program_signer_pubkey)
        .await
        .unwrap()
        .unwrap();

    let program_signer = mpl_migration_validator::state::ProgramSigner::try_from_slice(
        &program_signer_account.data[..],
    )
    .unwrap();

    assert_eq!(program_signer.bump, bump);

    context.warp_to_slot(1000).unwrap();

    // Cannot initialize again.
    let instruction = init_signer(context.payer.pubkey());

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&context.payer.pubkey()),
        &[&context.payer],
        context.last_blockhash,
    );

    let err = context
        .banks_client
        .process_transaction(transaction)
        .await
        .unwrap_err();

    assert_custom_error_ix!(0, err, MigrationError::AlreadyInitialized);
}


