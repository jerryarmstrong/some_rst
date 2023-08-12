test-program/tests/account-test.rs
==================================

Last edited: 2022-11-28 20:53:26

Contents:

.. code-block:: rs

    #![cfg(feature = "test-bpf")]

use solana_program_test::*;
use solana_sdk::{instruction::InstructionError, signer::Signer, transaction::TransactionError};
use test_program;
use solana_program_test::ProgramTest;

mod account_test {
    use solana_program::instruction::Instruction;
    use super::*;

    async fn context() -> ProgramTestContext {
        let p = ProgramTest::new(
            "test_program",
            test_program::id(),
            None,
        );
        p.start_with_context().await
    }

    #[tokio::test]
    async fn test_fail_fast() {
        let ctx = context().await;
        let ix = Instruction::new_with_bytes(
            test_program::id(),
            &[0, 0],
            vec![],
        );
        ctx.banks_client.
    }

    #[tokio::test]
    async fn test_consolidated_655truyrryufggsgr() {}
}


