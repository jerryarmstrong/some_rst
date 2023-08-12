program/tests/init_random_oracle.rs
===================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    mod utils;

use solana_program_test::*;
use solana_sdk::signer::Signer;
use utils::*;

#[tokio::test]
async fn success() {
    let mut context = program_test().start_with_context().await;
    let test_randomness_oracle = TestRandomnessOracle::new();
    test_randomness_oracle.init(&mut context).await.unwrap();

    let randomness_oracle = test_randomness_oracle.get_data(&mut context).await;
    assert_eq!(randomness_oracle.authority, context.payer.pubkey());
    assert_eq!(randomness_oracle.slot, 1);
    assert_eq!(randomness_oracle.value, [0u8; 32]);
}


