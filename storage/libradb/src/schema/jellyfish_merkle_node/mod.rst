storage/libradb/src/schema/jellyfish_merkle_node/mod.rs
=======================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module defines physical storage schema for nodes in the state Jellyfish Merkle Tree.
//! Node is identified by [NodeKey](solana_libra_jellyfish_merkle::node_type::NodeKey).
//! ```text
//! |<----key--->|<-----value----->|
//! |  node_key  | serialized_node |
//! ```

use crate::schema::JELLYFISH_MERKLE_NODE_CF_NAME;
use failure::prelude::*;
use solana_libra_jellyfish_merkle::node_type::{Node, NodeKey};
use solana_libra_schemadb::{
    define_schema,
    schema::{KeyCodec, ValueCodec},
};

define_schema!(
    JellyfishMerkleNodeSchema,
    NodeKey,
    Node,
    JELLYFISH_MERKLE_NODE_CF_NAME
);

impl KeyCodec<JellyfishMerkleNodeSchema> for NodeKey {
    fn encode_key(&self) -> Result<Vec<u8>> {
        self.encode()
    }

    fn decode_key(data: &[u8]) -> Result<Self> {
        Self::decode(data)
    }
}

impl ValueCodec<JellyfishMerkleNodeSchema> for Node {
    fn encode_value(&self) -> Result<Vec<u8>> {
        Ok(self.encode()?)
    }

    fn decode_value(data: &[u8]) -> Result<Self> {
        Ok(Self::decode(&data[..])?)
    }
}

#[cfg(test)]
mod test;


