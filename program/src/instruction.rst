program/src/instruction.rs
==========================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! Instruction states definitions.

use borsh::{BorshDeserialize, BorshSerialize};
use solana_program::{
    instruction::{AccountMeta, Instruction},
    pubkey::Pubkey,
    sysvar,
};

/// Instructions supported by the program.
#[derive(Debug, BorshDeserialize, BorshSerialize, PartialEq)]
pub enum RandomnessOracleInstruction {
    /// Initializes a new randomness oracle.
    ///
    /// Accounts:
    /// [W] Randomness oracle - off-chain created account.
    /// [RS] Authority - randomness oracle authority to update state.
    /// [R] Clock sysvar.
    InitRandomnessOracle,

    /// Updates randomness oracle.
    ///
    /// Accounts:
    /// [W] Randomness oracle - account.
    /// [RS] Authority - randomness oracle authority to update state.
    /// [R] Clock sysvar.
    UpdateRandomnessOracle { value: [u8; 32] },
}

/// Creates 'InitRandomnessOracle' instruction.
pub fn init_randomness_oracle(
    program_id: &Pubkey,
    randomness_oracle: &Pubkey,
    authority: &Pubkey,
) -> Instruction {
    let accounts = vec![
        AccountMeta::new(*randomness_oracle, false),
        AccountMeta::new_readonly(*authority, true),
        AccountMeta::new_readonly(sysvar::clock::id(), false),
    ];

    Instruction::new_with_borsh(
        *program_id,
        &RandomnessOracleInstruction::InitRandomnessOracle,
        accounts,
    )
}

/// Creates 'UpdateRandomnessOracle' instruction.
pub fn update_randomness_oracle(
    program_id: &Pubkey,
    randomness_oracle: &Pubkey,
    authority: &Pubkey,
    value: [u8; 32],
) -> Instruction {
    let accounts = vec![
        AccountMeta::new(*randomness_oracle, false),
        AccountMeta::new_readonly(*authority, true),
        AccountMeta::new_readonly(sysvar::clock::id(), false),
    ];

    Instruction::new_with_borsh(
        *program_id,
        &RandomnessOracleInstruction::UpdateRandomnessOracle { value },
        accounts,
    )
}


