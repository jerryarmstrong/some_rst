src/errors.rs
=============

Last edited: 2022-10-31 20:56:14

Contents:

.. code-block:: rs

    use thiserror::Error;

#[derive(Debug, Error)]
pub enum VtError {
    #[error("Client Error: {0}")]
    ClientError(String),
    #[error("Deserialization Error: {0}")]
    SerializationError(String),
    #[error("Conversion Error: {0}")]
    ConversionError(String),
    #[error("Signer Error: {0}")]
    SignerError(String),
}


