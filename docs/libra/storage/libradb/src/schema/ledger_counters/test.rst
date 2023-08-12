storage/libradb/src/schema/ledger_counters/test.rs
==================================================

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
    fn test_encode_decode(counters in any::<LedgerCounters>()) {
        assert_encode_decode::<LedgerCountersSchema>(&0, &counters);
    }
}


