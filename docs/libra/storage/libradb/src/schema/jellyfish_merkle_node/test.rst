storage/libradb/src/schema/jellyfish_merkle_node/test.rs
========================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use proptest::prelude::*;
use solana_libra_crypto::HashValue;
use solana_libra_jellyfish_merkle::node_type::Node;
use solana_libra_schemadb::schema::assert_encode_decode;
use solana_libra_types::account_state_blob::AccountStateBlob;

proptest! {
    #[test]
    fn test_jellyfish_merkle_node_schema(
        node_key in any::<NodeKey>(),
        account_key in any::<HashValue>(),
        blob in any::<AccountStateBlob>(),
    ) {
        assert_encode_decode::<JellyfishMerkleNodeSchema>(
            &node_key,
            &Node::new_leaf(account_key, blob),
        );
    }
}


