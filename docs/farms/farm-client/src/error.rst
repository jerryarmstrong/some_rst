farm-client/src/error.rs
========================

Last edited: 2022-12-05 19:44:34

Contents:

.. code-block:: rs

    use {
    pyth_client::PythError,
    solana_account_decoder::parse_account_data::ParseAccountError,
    solana_client::client_error::ClientError,
    solana_sdk::{program_error::ProgramError, pubkey::PubkeyError},
    thiserror::Error,
};

/// Farm Client Errors
#[derive(Debug, Error)]
pub enum FarmClientError {
    #[error(transparent)]
    RpcClientError(#[from] ClientError),
    #[error(transparent)]
    ProgramError(#[from] ProgramError),
    #[error(transparent)]
    ParseAccountError(#[from] ParseAccountError),
    #[error(transparent)]
    PubkeyError(#[from] PubkeyError),
    #[error(transparent)]
    PythError(#[from] PythError),
    #[error("Record not found: {0}")]
    RecordNotFound(String),
    #[error("ArrayString error: {0}")]
    ArrayStringError(String),
    #[error("I/O error: {0}")]
    IOError(String),
    #[error("Parse error: {0}")]
    ParseError(String),
    #[error("Value error: {0}")]
    ValueError(String),
    #[error("Insufficient balance: {0}")]
    InsufficientBalance(String),
}


