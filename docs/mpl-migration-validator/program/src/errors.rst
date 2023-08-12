program/src/errors.rs
=====================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    use num_derive::FromPrimitive;
use solana_program::{
    decode_error::DecodeError,
    msg,
    program_error::{PrintProgramError, ProgramError},
};
use thiserror::Error;

#[derive(Error, Clone, Copy, Debug, Eq, PartialEq, FromPrimitive)]
pub enum MigrationError {
    // 0, 0x0
    // #[error("Overflow error")]
    #[error("")]
    Overflow,

    // 1, 0x1
    // #[error("Failed to build Migrate instruction")]
    #[error("")]
    InvalidInstruction,

    // 2, 0x2
    // #[error("No rule set provided")]
    #[error("")]
    NoRuleSet,

    // 3, 0x3
    // #[error("This feature is currently disabled")]
    #[error("")]
    FeatureDisabled,

    // 4, 0x4
    // #[error("Invalid unlock method")]
    #[error("")]
    InvalidUnlockMethod,

    // Migration Errors

    // 5, 0x5
    // #[error("Cannot perform this action while migration is in progress")]
    #[error("")]
    MigrationInProgress,

    // 6, 0x6
    // #[error("Cannot be closed after migration has completed")]
    #[error("")]
    MigrationAlreadyCompleted,

    // 7, 0x7
    // #[error("Program signer is already initialized")]
    #[error("")]
    AlreadyInitialized,

    // 8, 0x8
    // #[error("Migration state account is locked")]
    #[error("")]
    MigrationLocked,

    // 9, 0x9
    // #[error("Immutable metadata cannot be migrated")]
    #[error("")]
    ImmutableMetadata,

    // 10, 0xA
    // #[error("Incorrect freeze authority")]
    #[error("")]
    IncorrectFreezeAuthority,

    // 11, 0xB
    // #[error("Incorrect token standard: must be NonFungible")]
    #[error("")]
    IncorrectTokenStandard,

    // 12, 0xC
    // #[error("Cannot migrate an item owned by an immutable program")]
    #[error("")]
    ImmutableProgramOwner,

    // Validation Errors

    // 13, 0xD
    // #[error("Metadata does not match mint account")]
    #[error("")]
    MetadataMintMistmatch,

    // 14, 0xE
    // #[error("Token does not match the mint account")]
    #[error("")]
    TokenMintMismatch,

    // 15 0xF
    // #[error("Collection mint does not match stored value")]
    #[error("")]
    CollectionMintMismatch,

    // 16 0x10
    // #[error("Authority does not match the authority on the account")]
    #[error("")]
    InvalidAuthority,

    // 17 0x11
    // #[error("No collection found on item")]
    #[error("")]
    CollectionNotFound,

    // 18 0x12
    // #[error("Item is not a verified member of the collection")]
    #[error("")]
    NotCollectionMember,

    // 19 0x13
    // #[error("Invalid token standard")]
    #[error("")]
    InvalidTokenStandard,

    // 20 0x14
    // #[error("Missing token standard")]
    #[error("")]
    MissingTokenStandard,

    // 21 0x15
    // #[error("The metadata derivation does not match the mint account")]
    #[error("")]
    InvalidMetadataDerivation,

    // 22 0x16
    // #[error("The edition derivation does not match the mint account")]
    #[error("")]
    InvalidEditionDerivation,

    // 23 0x17
    // #[error("Migration state account derivation is in correct")]
    #[error("")]
    InvalidMigrationStateDerivation,

    // 24 0x18
    // #[error("Program signer account derivation is incorrect")]
    #[error("")]
    InvalidSignerDerivation,

    // 25 0x19
    // #[error("Invalid delegate record derivation")]
    #[error("")]
    InvalidDelegateRecordDerivation,

    // 26 0x1A
    // #[error("Invalid delegate")]
    #[error("")]
    InvalidDelegate,

    // 27 0x1B
    // #[error("Incorrect program owner for metadata account")]
    #[error("")]
    IncorrectMetadataProgramOwner,

    // 28 0x1C
    // #[error("Incorrect program owner for mint account")]
    #[error("")]
    IncorrectMintProgramOwner,

    // 29 0x1D
    // #[error("Incorrect program owner for migration state account")]
    #[error("")]
    IncorrectMigrationStateProgramOwner,

    // 30 0x1E
    // #[error("Incorrect program owner for delegate record account")]
    #[error("")]
    IncorrectDelegateRecordProgramOwner,

    // 31 0x1F
    // #[error("Incorrect owner for SPL token account")]
    #[error("")]
    TokenOwnerMismatch,

    // 32 0x20
    // #[error("Incorrect program owner for token owner account")]
    #[error("")]
    IncorrectTokenOwnerProgramOwner,

    // 33 0x21
    // #[error("Incorrect program owner for token owner account buffer")]
    #[error("")]
    IncorrectTokenOwnerProgramBuffer,

    // Deserialization Errors

    // 34 0x22
    // #[error("Metadata did not deserialize correctly")]
    #[error("")]
    InvalidMetadata,

    // 35 0x23
    // #[error("Migration state did not deserialize correctly")]
    #[error("")]
    InvalidMigrationState,

    // 36 0x24
    // #[error("Empty migration state account")]
    #[error("")]
    EmptyMigrationState,

    // 37 0x25
    // #[error("Zeroed migration state account")]
    #[error("")]
    ZeroedMigrationState,

    // 38 0x26
    // #[error("Program signer did not deserialize correctly")]
    #[error("")]
    InvalidProgramSigner,

    // 39 0x27
    // #[error("Empty program signer account")]
    #[error("")]
    EmptyProgramSigner,

    // 40 0x28
    // #[error("Failed to deserialize UpgradeableLoaderState")]
    #[error("")]
    InvalidUpgradeableLoaderState,

    // 41 0x29
    // #[error("Authorization rules does not match the rule set stored on the state")]
    #[error("")]
    InvalidRuleSet,

    /// 42 0x2A
    #[error("This instruction has been deprecated")]
    DeprecatedInstruction,
}

// Migration Error Impls
impl PrintProgramError for MigrationError {
    fn print<E>(&self) {
        msg!("Error {}: {}", *self as u32, &self.to_string());
    }
}

impl From<MigrationError> for ProgramError {
    fn from(e: MigrationError) -> Self {
        ProgramError::Custom(e as u32)
    }
}

impl<T> DecodeError<T> for MigrationError {
    fn type_of() -> &'static str {
        "Migration Error"
    }
}


