programs/auto-emissions/src/error.rs
====================================

Last edited: 2023-08-01 15:01:51

Contents:

.. code-block:: rs

    //! Error types

use anchor_lang::prelude::*;

#[error_code]
pub enum AutoEmissionsError {
    #[msg("Invalid authority")]
    InvalidAuthority,
    #[msg("Overflow in arithmetic operation")]
    MathOverflow,
    #[msg("Invalid group state")]
    InvalidGroupState,
    #[msg("Invalid protocol config")]
    InvalidProtocolConfig,
    #[msg("Invalid group config")]
    InvalidGroupConfig,
    #[msg("Invalid participant config")]
    InvalidParticipantConfig,
    #[msg("Invalid group address")]
    InvalidGroupAddress,
    #[msg("Invalid custody address")]
    InvalidCustodyAddress,
    #[msg("Instruction is not allowed at this time")]
    InstructionNotAllowed,
    #[msg("Instruction is not allowed in production")]
    InvalidEnvironment,
}


