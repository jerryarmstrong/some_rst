shank-idl/src/idl_metadata.rs
=============================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct IdlMetadata {
    /// shank
    pub origin: String,
    #[serde(skip_serializing_if = "Option::is_none", default)]
    pub address: Option<String>,
}


