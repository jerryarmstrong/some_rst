storage/libradb/src/schema/event_accumulator/test.rs
====================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use solana_libra_schemadb::schema::assert_encode_decode;

#[test]
fn test_encode_decode() {
    assert_encode_decode::<EventAccumulatorSchema>(
        &(100, Position::from_inorder_index(100)),
        &HashValue::random(),
    );
}


