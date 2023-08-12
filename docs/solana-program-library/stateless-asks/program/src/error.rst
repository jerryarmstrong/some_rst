stateless-asks/program/src/error.rs
===================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    use thiserror::Error;

use solana_program::program_error::ProgramError;

#[derive(Error, Debug, Copy, Clone)]
pub enum UtilError {
    #[error("PublicKeyMismatch")]
    PublicKeyMismatch,
    #[error("InvalidMintAuthority")]
    InvalidMintAuthority,
    #[error("UninitializedAccount")]
    UninitializedAccount,
    #[error("IncorrectOwner")]
    IncorrectOwner,
    #[error("PublicKeysShouldBeUnique")]
    PublicKeysShouldBeUnique,
    #[error("StatementFalse")]
    StatementFalse,
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


