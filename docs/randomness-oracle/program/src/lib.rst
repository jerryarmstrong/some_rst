program/src/lib.rs
==================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    pub mod instruction;
pub mod processor;
pub mod state;
mod utils;

#[cfg(not(feature = "no-entrypoint"))]
pub mod entrypoint;

// Export current sdk types for downstream users building with a different sdk version.
pub use solana_program;
use solana_program::{
    account_info::AccountInfo, clock::Slot, program_error::ProgramError, program_pack::Pack,
};
use state::RandomnessOracle;

solana_program::declare_id!("mrnd3eZc5ctZm9vmG6JRFaU4TinYMeApRRWYPS6dhyW");

pub fn read_value(randomness_oracle_info: &AccountInfo) -> Result<([u8; 32], Slot), ProgramError> {
    let RandomnessOracle { value, slot, .. } =
        RandomnessOracle::unpack(&randomness_oracle_info.data.borrow())?;

    Ok((value, slot))
}


