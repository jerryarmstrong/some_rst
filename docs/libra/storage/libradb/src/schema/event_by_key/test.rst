storage/libradb/src/schema/event_by_key/test.rs
===============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use proptest::prelude::*;
use solana_libra_schemadb::schema::assert_encode_decode;

proptest! {
    #[test]
    fn test_encode_decode(
        event_key in any::<EventKey>(),
        seq_num in any::<u64>(),
        version in any::<Version>(),
        index in any::<u64>(),
    ) {
        assert_encode_decode::<EventByKeySchema>(&(event_key, seq_num), &(version, index));
    }
}


