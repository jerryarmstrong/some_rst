examples/eggs/src/state.rs
==========================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! State types

use super::*;
use borsh::{BorshDeserialize, BorshSchema, BorshSerialize};
use solana_program::{
    msg,
    program_error::ProgramError,
    program_pack::{IsInitialized, Pack, Sealed},
};

/// Enum representing the account type managed by the program
#[derive(Clone, Debug, PartialEq, BorshDeserialize, BorshSerialize, BorshSchema)]
pub enum AccountType {
    /// If the account has not been initialized, the enum will be 0
    Uninitialized,
    /// Egg
    Egg,
}

impl Default for AccountType {
    fn default() -> Self {
        AccountType::Uninitialized
    }
}

/// Egg
#[repr(C)]
#[derive(Debug, BorshSerialize, BorshDeserialize, BorshSchema, Default)]
pub struct Egg {
    /// Account type - Egg
    pub account_type: AccountType,
    /// Gen value
    pub gen: [u8; 32],
}

impl Egg {
    /// Initialize a Egg
    pub fn init(&mut self, params: InitEggParams) {
        self.account_type = AccountType::Egg;
        self.gen = params.gen;
    }
}

/// Initialize a Egg params
pub struct InitEggParams {
    /// Gen value
    pub gen: [u8; 32],
}

impl Sealed for Egg {}

impl Pack for Egg {
    // 1 + 32
    const LEN: usize = 33;

    fn pack_into_slice(&self, dst: &mut [u8]) {
        let mut slice = dst;
        self.serialize(&mut slice).unwrap()
    }

    fn unpack_from_slice(src: &[u8]) -> Result<Self, ProgramError> {
        Self::try_from_slice(src).map_err(|_| {
            msg!("Failed to deserialize");
            ProgramError::InvalidAccountData
        })
    }
}

impl IsInitialized for Egg {
    fn is_initialized(&self) -> bool {
        self.account_type != AccountType::Uninitialized && self.account_type == AccountType::Egg
    }
}


