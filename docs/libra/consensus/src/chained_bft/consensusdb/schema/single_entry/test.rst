consensus/src/chained_bft/consensusdb/schema/single_entry/test.rs
=================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use solana_libra_schemadb::schema::assert_encode_decode;

#[test]
fn test_single_entry_schema() {
    assert_encode_decode::<SingleEntrySchema>(
        &SingleEntryKey::ConsensusState,
        &vec![1u8, 2u8, 3u8],
    );
}


