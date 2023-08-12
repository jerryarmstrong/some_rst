examples/eggs/tests/create_egg.rs
=================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]

mod utils;

use solana_program::pubkey::Pubkey;
use solana_program_test::*;
use std::str::FromStr;
use utils::*;

const ORACLE_VALUE: [u8; 32] = [
    21, 55, 34, 118, 215, 173, 121, 153, 252, 95, 48, 178, 57, 189, 58, 113, 84, 254, 7, 95, 122,
    136, 28, 185, 222, 127, 206, 122, 239, 245, 101, 22,
];

async fn setup() -> (ProgramTestContext, TestOracle) {
    let mut test = program_test();
    let oracle = add_oracle(
        &mut test,
        Pubkey::from_str("FjvDD58C8Su9Uq92dztpUpAkoY9dzAf3HiwUxbpMkcru").unwrap(),
    );
    let context = test.start_with_context().await;

    (context, oracle)
}

#[tokio::test]
async fn success() {
    let (mut context, test_oracle) = setup().await;

    let test_egg = TestEgg::new();
    test_egg.create(&mut context, &test_oracle).await.unwrap();

    let egg = test_egg.get_data(&mut context).await;

    assert_eq!(egg.gen, ORACLE_VALUE);
}


