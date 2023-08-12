programs/dummy-oracle/src/error.rs
==================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: rs

    use thiserror::Error;

use solana_program::program_error::ProgramError;

#[derive(Error, Debug, Copy, Clone)]
pub enum UtilError {
    #[error("PublicKeyMismatch")]
    PublicKeyMismatch,
    #[error("AssertionError")]
    AssertionError,
    #[error("InvalidMintAuthority")]
    InvalidMintAuthority,
    #[error("AccountUninitialized")]
    AccountUninitialized,
    #[error("IncorrectOwner")]
    IncorrectOwner,
    #[error("PublicKeysShouldBeUnique")]
    PublicKeysShouldBeUnique,
    #[error("NotRentExempt")]
    NotRentExempt,
    #[error("NumericalOverflow")]
    NumericalOverflow,
}

impl From<UtilError> for ProgramError {
    fn from(e: UtilError) -> Self {
        ProgramError::Custom(e as u32)
    }
}


