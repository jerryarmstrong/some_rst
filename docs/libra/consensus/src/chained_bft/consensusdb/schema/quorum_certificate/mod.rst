consensus/src/chained_bft/consensusdb/schema/quorum_certificate/mod.rs
======================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module defines physical storage schema for consensus quorum certificate (of a block).
//!
//! Serialized quorum certificate bytes identified by block_hash.
//! ```text
//! |<---key---->|<----value--->|
//! | block_hash |  QuorumCert  |
//! ```

use super::QC_CF_NAME;
use crate::chained_bft::consensus_types::quorum_cert::QuorumCert;
use failure::prelude::*;
use prost::Message;
use solana_libra_crypto::HashValue;
use solana_libra_prost_ext::MessageExt;
use solana_libra_schemadb::{
    define_schema,
    schema::{KeyCodec, ValueCodec},
};
use std::convert::TryInto;

define_schema!(QCSchema, HashValue, QuorumCert, QC_CF_NAME);

impl KeyCodec<QCSchema> for HashValue {
    fn encode_key(&self) -> Result<Vec<u8>> {
        Ok(self.to_vec())
    }

    fn decode_key(data: &[u8]) -> Result<Self> {
        Ok(HashValue::from_slice(data)?)
    }
}

impl ValueCodec<QCSchema> for QuorumCert {
    fn encode_value(&self) -> Result<Vec<u8>> {
        let cert: solana_libra_network::proto::QuorumCert = self.clone().into();
        Ok(cert.to_vec()?)
    }

    fn decode_value(data: &[u8]) -> Result<Self> {
        solana_libra_network::proto::QuorumCert::decode(data)?.try_into()
    }
}

#[cfg(test)]
mod test;


