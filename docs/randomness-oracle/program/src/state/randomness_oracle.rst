program/src/state/randomness_oracle.rs
======================================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! Random oracle state definitions.

use borsh::{BorshDeserialize, BorshSchema, BorshSerialize};
use solana_program::{
    clock::Slot,
    msg,
    program_error::ProgramError,
    program_pack::{IsInitialized, Pack, Sealed},
    pubkey::Pubkey,
};

use super::AccountType;

/// Random oracle initialization params.
pub struct InitRandomnessOracleParams {
    /// Authority.
    pub authority: Pubkey,
    /// Current slot.
    pub slot: Slot,
}

/// Random oracle.
#[repr(C)]
#[derive(Debug, Clone, BorshDeserialize, BorshSerialize, BorshSchema, PartialEq, Default)]
pub struct RandomnessOracle {
    /// Account type.
    pub account_type: AccountType,
    /// Authority.
    pub authority: Pubkey,
    /// Random value.
    pub value: [u8; 32],
    /// Last slot.
    pub slot: Slot,
}

impl RandomnessOracle {
    /// Initialize a random oracle.
    pub fn init(&mut self, params: InitRandomnessOracleParams) {
        self.account_type = AccountType::RandomnessOracle;
        self.authority = params.authority;
        self.value = [0u8; 32];
        self.slot = params.slot;
    }

    /// Update random oracle.
    pub fn update(&mut self, value: [u8; 32], slot: Slot) {
        self.value = value;
        self.slot = slot;
    }
}

impl Sealed for RandomnessOracle {}

impl Pack for RandomnessOracle {
    // 1 + 32 + 32 + 8
    const LEN: usize = 73;

    fn pack_into_slice(&self, dst: &mut [u8]) {
        let mut slice = dst;
        self.serialize(&mut slice).unwrap()
    }

    fn unpack_from_slice(src: &[u8]) -> Result<Self, ProgramError> {
        Self::try_from_slice(src).map_err(|_| {
            msg!("Failed to deserialize");
            msg!("Actual LEN: {}", std::mem::size_of::<RandomnessOracle>());
            ProgramError::InvalidAccountData
        })
    }
}

impl IsInitialized for RandomnessOracle {
    fn is_initialized(&self) -> bool {
        self.account_type == AccountType::RandomnessOracle
    }
}


