examples/eggs/tests/utils/mod.rs
================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use eggs::{id, processor};
use solana_program::pubkey::Pubkey;
use solana_program_test::*;
use solana_program_test::{ProgramTest, ProgramTestContext};
use solana_sdk::account::Account;

pub mod egg;
pub mod oracle;

pub use egg::*;
pub use oracle::*;

pub fn program_test() -> ProgramTest {
    ProgramTest::new(
        "eggs",
        id(),
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


