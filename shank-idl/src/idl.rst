shank-idl/src/idl.rs
====================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    /// NOTE: this was lifted from https://github.com/project-serum/anchor/blob/1a2fd38451b36a569287eb9794ec10e51675789e/lang/syn/src/idl/mod.rs
/// We want to add non-anchor specific extensions to this IDL which is why we don't depend on the
/// anchor crate instead.
use serde::{Deserialize, Serialize};

use crate::{
    idl_error_code::IdlErrorCode, idl_instruction::IdlInstruction,
    idl_metadata::IdlMetadata,
};

use super::{idl_type::IdlType, idl_type_definition::IdlTypeDefinition};
use anyhow::{anyhow, Result};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct Idl {
    pub version: String,
    pub name: String,
    #[serde(skip_serializing_if = "Vec::is_empty", default)]
    pub constants: Vec<IdlConst>,
    pub instructions: Vec<IdlInstruction>,
    #[serde(skip_serializing_if = "Option::is_none", default)]
    pub state: Option<IdlState>,
    #[serde(skip_serializing_if = "Vec::is_empty", default)]
    pub accounts: Vec<IdlTypeDefinition>,
    #[serde(skip_serializing_if = "Vec::is_empty", default)]
    pub types: Vec<IdlTypeDefinition>,
    #[serde(skip_serializing_if = "Option::is_none", default)]
    pub events: Option<Vec<IdlEvent>>,
    #[serde(skip_serializing_if = "Option::is_none", default)]
    pub errors: Option<Vec<IdlErrorCode>>,
    pub metadata: IdlMetadata,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct IdlConst {
    pub name: String,
    #[serde(rename = "type")]
    pub ty: IdlType,
    pub value: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct IdlState {
    #[serde(rename = "struct")]
    pub strct: IdlTypeDefinition,
    pub methods: Vec<IdlInstruction>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct IdlEvent {
    pub name: String,
    pub fields: Vec<IdlEventField>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub struct IdlEventField {
    pub name: String,
    #[serde(rename = "type")]
    pub ty: IdlType,
    pub index: bool,
}

impl Idl {
    pub fn try_into_json(&self) -> Result<String> {
        serde_json::to_string_pretty(&self)
            .map_err(|err| anyhow!("Failed to convert to JSON. {}", err))
    }
}


