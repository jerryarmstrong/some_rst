consensus/src/chained_bft/consensusdb/schema/block/mod.rs
=========================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module defines physical storage schema for consensus block.
//!
//! Serialized block bytes identified by block_hash.
//! ```text
//! |<---key---->|<---value--->|
//! | block_hash |    block    |
//! ```

use super::BLOCK_CF_NAME;
use crate::chained_bft::{common::Payload, consensus_types::block::Block};
use failure::prelude::*;
use prost::Message;
use solana_libra_crypto::HashValue;
use solana_libra_prost_ext::MessageExt;
use solana_libra_schemadb::schema::{KeyCodec, Schema, ValueCodec};
use std::convert::TryInto;
use std::marker::PhantomData;

pub struct BlockSchema<T: Payload> {
    phantom: PhantomData<T>,
}

impl<T: Payload> Schema for BlockSchema<T> {
    const COLUMN_FAMILY_NAME: solana_libra_schemadb::ColumnFamilyName = BLOCK_CF_NAME;
    type Key = HashValue;
    type Value = Block<T>;
}

impl<T: Payload> KeyCodec<BlockSchema<T>> for HashValue {
    fn encode_key(&self) -> Result<Vec<u8>> {
        Ok(self.to_vec())
    }

    fn decode_key(data: &[u8]) -> Result<Self> {
        Ok(HashValue::from_slice(data)?)
    }
}

impl<T: Payload> ValueCodec<BlockSchema<T>> for Block<T> {
    fn encode_value(&self) -> Result<Vec<u8>> {
        let block: solana_libra_network::proto::Block = self.clone().into();
        Ok(block.to_vec()?)
    }

    fn decode_value(data: &[u8]) -> Result<Self> {
        solana_libra_network::proto::Block::decode(data)?.try_into()
    }
}

#[cfg(test)]
mod test;


