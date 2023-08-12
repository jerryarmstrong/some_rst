program/tests/utils/mod.rs
==========================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    #![allow(dead_code)]

mod test_randomness_oracle;

use randomness_oracle_program::processor;
use solana_program::pubkey::Pubkey;
use solana_program_test::*;
use solana_sdk::account::Account;
pub use test_randomness_oracle::*;

pub fn program_test() -> ProgramTest {
    ProgramTest::new(
        "randomness_oracle_program",
        randomness_oracle_program::id(),
        processor!(processor::Processor::process_instruction),
    )
}

pub async fn get_account(context: &mut ProgramTestContext, pubkey: &Pubkey) -> Account {
    context
        .banks_client
        .get_account(*pubkey)
        .await
        .expect("account not found")
        .expect("account empty")
}


