types/src/transaction/program.rs
================================

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

#[derive(Clone, Hash, Eq, PartialEq, Serialize, Deserialize)]
pub struct Program {
    code: Vec<u8>,
    args: Vec<TransactionArgument>,
    modules: Vec<Vec<u8>>,
}

impl Program {
    pub fn new(code: Vec<u8>, modules: Vec<Vec<u8>>, args: Vec<TransactionArgument>) -> Program {
        Program {
            code,
            modules,
            args,
        }
    }

    pub fn code(&self) -> &[u8] {
        &self.code
    }

    pub fn args(&self) -> &[TransactionArgument] {
        &self.args
    }

    pub fn modules(&self) -> &[Vec<u8>] {
        &self.modules
    }

    pub fn into_inner(self) -> (Vec<u8>, Vec<TransactionArgument>, Vec<Vec<u8>>) {
        (self.code, self.args, self.modules)
    }
}

impl fmt::Debug for Program {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Program")
            .field("code", &hex::encode(&self.code))
            .field("args", &self.args)
            .finish()
    }
}

impl CanonicalSerialize for Program {
    fn serialize(&self, serializer: &mut impl CanonicalSerializer) -> Result<()> {
        serializer.encode_vec(&self.code)?;
        serializer.encode_vec(&self.args)?;
        serializer.encode_vec(&self.modules)?;
        Ok(())
    }
}

impl CanonicalDeserialize for Program {
    fn deserialize(deserializer: &mut impl CanonicalDeserializer) -> Result<Self> {
        let code: Vec<u8> = deserializer.decode_vec()?;
        let args: Vec<TransactionArgument> = deserializer.decode_vec()?;
        let modules: Vec<Vec<u8>> = deserializer.decode_vec()?;

        Ok(Program::new(code, modules, args))
    }
}


