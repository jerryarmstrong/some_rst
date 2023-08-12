program/tests/update_random_oracle.rs
=====================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    mod utils;

use solana_program_test::*;
use solana_sdk::signer::Signer;
use utils::*;

async fn setup() -> (ProgramTestContext, TestRandomnessOracle) {
    let mut context = program_test().start_with_context().await;

    let test_randomness_oracle = TestRandomnessOracle::new();
    test_randomness_oracle.init(&mut context).await.unwrap();

    (context, test_randomness_oracle)
}

#[tokio::test]
async fn success() {
    let (mut context, test_randomness_oracle) = setup().await;
    context.warp_to_slot(3).unwrap();

    test_randomness_oracle
        .update(&mut context, [1u8; 32])
        .await
        .unwrap();

    let randomness_oracle = test_randomness_oracle.get_data(&mut context).await;
    assert_eq!(randomness_oracle.authority, context.payer.pubkey());
    assert_eq!(randomness_oracle.slot, 3);
    assert_eq!(randomness_oracle.value, [1u8; 32]);
}


