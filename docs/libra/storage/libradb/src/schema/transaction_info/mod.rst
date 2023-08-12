storage/libradb/src/schema/transaction_info/mod.rs
==================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module defines physical storage schema for TransactionInfo structure.
//!
//! Serialized signed transaction bytes identified by version.
//! ```text
//! |<--key-->|<-----value---->|
//! | version | txn_info bytes |
//! ```
//!
//! `Version` is serialized in big endian so that records in RocksDB will be in order of it's
//! numeric value.

use crate::schema::TRANSACTION_INFO_CF_NAME;
use byteorder::{BigEndian, ReadBytesExt};
use failure::prelude::*;
use prost::Message;
use solana_libra_prost_ext::MessageExt;
use solana_libra_schemadb::{
    define_schema,
    schema::{KeyCodec, ValueCodec},
};
use solana_libra_types::transaction::{TransactionInfo, Version};
use std::convert::TryInto;
use std::mem::size_of;

define_schema!(
    TransactionInfoSchema,
    Version,
    TransactionInfo,
    TRANSACTION_INFO_CF_NAME
);

impl KeyCodec<TransactionInfoSchema> for Version {
    fn encode_key(&self) -> Result<Vec<u8>> {
        Ok(self.to_be_bytes().to_vec())
    }

    fn decode_key(data: &[u8]) -> Result<Self> {
        ensure!(
            data.len() == size_of::<Version>(),
            "Bad num of bytes: {}",
            data.len()
        );
        Ok((&data[..]).read_u64::<BigEndian>()?)
    }
}

impl ValueCodec<TransactionInfoSchema> for TransactionInfo {
    fn encode_value(&self) -> Result<Vec<u8>> {
        let event: solana_libra_types::proto::types::TransactionInfo = self.clone().into();
        Ok(event.to_vec()?)
    }

    fn decode_value(data: &[u8]) -> Result<Self> {
        solana_libra_types::proto::types::TransactionInfo::decode(data)?.try_into()
    }
}

#[cfg(test)]
mod test;


