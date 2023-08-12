programs/system-extras/src/error.rs
===================================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: rs

    use num_derive::FromPrimitive;
use solana_program::{
    decode_error::DecodeError,
    msg,
    program_error::{PrintProgramError, ProgramError},
};
use thiserror::Error;

#[derive(Error, Clone, Debug, Eq, PartialEq, FromPrimitive)]
pub enum SystemExtrasError {
    #[error("Invalid System Program")]
    InvalidSystemProgram,
    #[error("Invalid Program Owner For The Source Account")]
    InvalidOwnerForSource,
}

impl PrintProgramError for SystemExtrasError {
    fn print<E>(&self) {
        msg!(&self.to_string());
    }
}

impl From<SystemExtrasError> for ProgramError {
    fn from(e: SystemExtrasError) -> Self {
        ProgramError::Custom(e as u32)
    }
}

impl<T> DecodeError<T> for SystemExtrasError {
    fn type_of() -> &'static str {
        "Create With Rent Error"
    }
}


