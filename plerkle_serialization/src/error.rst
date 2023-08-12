plerkle_serialization/src/error.rs
==================================

Last edited: 2023-08-03 21:06:53

Contents:

.. code-block:: rs

    use thiserror::Error;
#[derive(Debug, Clone, PartialEq, Eq,Error)]
pub enum PlerkleSerializationError {
    #[error("Serialization error: {0}")]
    SerializationError(String)
}

