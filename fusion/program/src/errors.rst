fusion/program/src/errors.rs
============================

Last edited: 2022-04-29 15:13:47

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

#[error]
pub enum ErrorCode {
    #[msg("Invalid remaining accounts length")]
    InvalidRemainingAccountsLength,
    #[msg("Invalid token mint")]
    InvalidMint,
    #[msg("Invalid token amount")]
    InvalidAmount,
    #[msg("Invalid token authority")]
    InvalidAuthority,
    #[msg("TokenAccount must be owned by the output mint authority PDA")]
    TokenAccountOwnerMustBeOutputMintAuthority,
    #[msg("Master Token account does not matched derived address")]
    MasterTokenAccountMismatch,
    #[msg("Invalid token metadata program")]
    InvalidTokenMetadataProgram
}


