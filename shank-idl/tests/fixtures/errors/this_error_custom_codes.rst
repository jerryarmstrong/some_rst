shank-idl/tests/fixtures/errors/this_error_custom_codes.rs
==========================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    /// Errors that may be returned by the Vault program.
#[derive(Clone, Debug, Eq, Error, FromPrimitive, PartialEq)]
pub enum VaultError {
    /// Invalid instruction data passed in.
    #[error("Failed to unpack instruction data")]
    InstructionUnpackError = 3000,

    /// Lamport balance below rent-exempt threshold.
    #[error("Lamport balance below rent-exempt threshold")]
    NotRentExempt,

    /// Already initialized
    #[error("Already initialized")]
    AlreadyInitialized,

    /// Uninitialized
    #[error("Uninitialized")]
    Uninitialized,

    /// Account does not have correct owner
    #[error("Account does not have correct owner")]
    IncorrectOwner = 4000,

    /// NumericalOverflowError
    #[error("NumericalOverflowError")]
    NumericalOverflowError,
}


