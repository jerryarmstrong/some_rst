program/src/state.rs
====================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use std::str::FromStr;

use borsh::{BorshDeserialize, BorshSerialize};
use shank::ShankAccount;
use solana_program::{
    account_info::AccountInfo, program_error::ProgramError, program_memory::sol_memcpy, pubkey,
    pubkey::Pubkey,
};

#[cfg(feature = "serde-feature")]
use {
    serde::{Deserialize, Serialize},
    serde_with::{As, DisplayFromStr},
};

use crate::errors::MigrationError;

pub(crate) const SPL_TOKEN_ID: Pubkey = pubkey!("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA");

#[cfg_attr(feature = "serde-feature", derive(Serialize, Deserialize))]
#[derive(Clone, BorshSerialize, BorshDeserialize, Debug, ShankAccount)]
// Seeds: [b"migration", collection_mint.as_ref()]
pub struct MigrationState {
    pub collection_info: CollectionInfo,
    pub unlock_method: UnlockMethod,
    pub status: MigrationStatus,
}

/// See if a slice contains all zeroes.  Useful for checking an account's data.
pub fn is_zeroed_chunks(buf: &[u8]) -> bool {
    const ZEROS_LEN: usize = 1024;
    const ZEROS: [u8; ZEROS_LEN] = [0; ZEROS_LEN];
    let mut chunks = buf.chunks_exact(ZEROS_LEN);

    {
        chunks.all(|chunk| chunk == &ZEROS[..])
            && chunks.remainder() == &ZEROS[..chunks.remainder().len()]
    }
}

impl MigrationState {
    pub fn from_account_info(a: &AccountInfo) -> Result<Self, ProgramError> {
        let data = a.try_borrow_data()?;

        if data.is_empty() {
            return Err(MigrationError::EmptyMigrationState.into());
        }

        if is_zeroed_chunks(&data) {
            return Err(MigrationError::ZeroedMigrationState.into());
        }

        let ua = <Self as BorshDeserialize>::deserialize(&mut data.as_ref())
            .map_err(|_| MigrationError::InvalidMigrationState)?;

        Ok(ua)
    }

    pub fn save(&self, a: &AccountInfo) -> Result<(), ProgramError> {
        let serialized_data = self.try_to_vec()?;
        let data_len = serialized_data.len();

        sol_memcpy(
            &mut a.data.borrow_mut(),
            serialized_data.as_slice(),
            data_len,
        );

        Ok(())
    }
}

impl Default for MigrationState {
    fn default() -> Self {
        Self {
            collection_info: CollectionInfo::default(),
            unlock_method: UnlockMethod::Timed,
            status: MigrationStatus::default(),
        }
    }
}

#[cfg_attr(feature = "serde-feature", derive(Serialize, Deserialize))]
#[derive(Clone, Default, BorshSerialize, BorshDeserialize, Debug, ShankAccount)]
pub struct CollectionInfo {
    #[cfg_attr(feature = "serde-feature", serde(with = "As::<DisplayFromStr>"))]
    pub authority: Pubkey,

    #[cfg_attr(feature = "serde-feature", serde(with = "As::<DisplayFromStr>"))]
    pub mint: Pubkey,

    #[cfg_attr(feature = "serde-feature", serde(with = "As::<DisplayFromStr>"))]
    pub rule_set: Pubkey,

    #[cfg_attr(feature = "serde-feature", serde(with = "As::<DisplayFromStr>"))]
    pub delegate_record: Pubkey,

    pub size: u32,
}

#[cfg_attr(feature = "serde-feature", derive(Serialize, Deserialize))]
#[derive(Clone, Default, BorshSerialize, BorshDeserialize, Debug, ShankAccount)]
pub struct MigrationStatus {
    pub unlock_time: i64,
    pub is_locked: bool,
    pub in_progress: bool,
    pub items_migrated: u32,
}

#[cfg_attr(feature = "serde-feature", derive(Serialize, Deserialize))]
#[derive(Copy, Clone, BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug)]
pub enum UnlockMethod {
    Timed,
    Vote,
}

impl FromStr for UnlockMethod {
    type Err = MigrationError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_lowercase().as_str() {
            "timed" => Ok(UnlockMethod::Timed),
            "vote" => Ok(UnlockMethod::Vote),
            _ => Err(MigrationError::InvalidUnlockMethod),
        }
    }
}

#[derive(Clone, BorshSerialize, BorshDeserialize, Debug, ShankAccount)]
pub struct ProgramSigner {
    pub bump: u8,
}

impl ProgramSigner {
    pub fn from_account_info(a: &AccountInfo) -> Result<Self, ProgramError> {
        let data = a.try_borrow_data()?;

        if data.is_empty() {
            return Err(MigrationError::EmptyProgramSigner.into());
        }

        let ua = Self::deserialize(&mut data.as_ref())
            .map_err(|_| MigrationError::InvalidProgramSigner)?;

        Ok(ua)
    }
}


