examples/eggs/src/instruction.rs
================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! Instruction types

use borsh::{BorshDeserialize, BorshSerialize};
use solana_program::{
    instruction::{AccountMeta, Instruction},
    pubkey::Pubkey,
    sysvar,
};

/// Instructions supported by the program
#[derive(Debug, BorshDeserialize, BorshSerialize, PartialEq)]
pub enum EggsInstruction {
    /// Create a new egg
    ///
    /// Accounts:
    /// [W] Egg - uninitialized
    /// [R] Randomness oracle
    /// [R] Rent sysvar
    CreateEgg,
}

/// Creates 'CreateEgg' instruction.
#[allow(clippy::too_many_arguments)]
pub fn create_egg(program_id: &Pubkey, egg: &Pubkey, randomness_oracle: &Pubkey) -> Instruction {
    let accounts = vec![
        AccountMeta::new(*egg, false),
        AccountMeta::new_readonly(*randomness_oracle, false),
        AccountMeta::new_readonly(sysvar::rent::id(), false),
    ];

    Instruction::new_with_borsh(*program_id, &EggsInstruction::CreateEgg, accounts)
}


