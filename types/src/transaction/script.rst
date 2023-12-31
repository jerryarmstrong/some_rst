types/src/transaction/script.rs
===============================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::transaction::transaction_argument::TransactionArgument;
use failure::prelude::*;
use serde::{Deserialize, Serialize};
use solana_libra_canonical_serialization::{
    CanonicalDeserialize, CanonicalDeserializer, CanonicalSerialize, CanonicalSerializer,
};
use std::fmt;

#[allow(dead_code)]
pub const SCRIPT_HASH_LENGTH: usize = 32;

#[derive(Clone, Hash, Eq, PartialEq, Serialize, Deserialize)]
pub struct Script {
    code: Vec<u8>,
    args: Vec<TransactionArgument>,
}

impl Script {
    pub fn new(code: Vec<u8>, args: Vec<TransactionArgument>) -> Self {
        Script { code, args }
    }

    pub fn code(&self) -> &[u8] {
        &self.code
    }

    pub fn args(&self) -> &[TransactionArgument] {
        &self.args
    }

    pub fn into_inner(self) -> (Vec<u8>, Vec<TransactionArgument>) {
        (self.code, self.args)
    }
}

impl fmt::Debug for Script {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Script")
            .field("code", &hex::encode(&self.code))
            .field("args", &self.args)
            .finish()
    }
}

impl CanonicalSerialize for Script {
    fn serialize(&self, serializer: &mut impl CanonicalSerializer) -> Result<()> {
        serializer.encode_vec(&self.code)?;
        serializer.encode_vec(&self.args)?;
        Ok(())
    }
}

impl CanonicalDeserialize for Script {
    fn deserialize(deserializer: &mut impl CanonicalDeserializer) -> Result<Self> {
        let code: Vec<u8> = deserializer.decode_vec()?;
        let args: Vec<TransactionArgument> = deserializer.decode_vec()?;
        Ok(Script::new(code, args))
    }
}


