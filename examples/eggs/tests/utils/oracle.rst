examples/eggs/tests/utils/oracle.rs
===================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    use solana_program::pubkey::Pubkey;
use solana_program_test::ProgramTest;
use solana_sdk::{signature::Keypair, signer::Signer};

const ORACLE_SECRET: &[u8] = &[
    146, 187, 161, 254, 149, 156, 131, 49, 20, 215, 236, 125, 11, 57, 239, 151, 252, 67, 171, 247,
    61, 223, 33, 194, 246, 61, 86, 246, 85, 133, 38, 105, 217, 227, 198, 249, 83, 86, 93, 141, 21,
    82, 28, 179, 207, 157, 142, 235, 170, 57, 244, 195, 221, 89, 129, 235, 34, 224, 123, 206, 156,
    124, 20, 242,
];

#[derive(Debug, Clone, Copy)]
pub struct TestOracle {
    pub pubkey: Pubkey,
}

pub fn add_oracle(test: &mut ProgramTest, pubkey: Pubkey) -> TestOracle {
    let oracle_program = Keypair::from_bytes(ORACLE_SECRET).unwrap();

    // Add randomness oracle account
    test.add_account_with_file_data(
        pubkey,
        u32::MAX as u64,
        oracle_program.pubkey(),
        &format!("{}.bin", pubkey.to_string()),
    );

    TestOracle { pubkey }
}


