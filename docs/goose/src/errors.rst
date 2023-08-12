src/errors.rs
=============

Last edited: 2023-06-13 21:53:04

Contents:

.. code-block:: rs

    use thiserror::Error;

#[derive(Error, Debug)]
pub enum CliError {
    #[error("Invalid unlock method. Must be one of: Timed, Vote")]
    InvalidUnlockMethod,
    #[error("No Solana CLI config file found.")]
    MissingSolanaConfig,
}


