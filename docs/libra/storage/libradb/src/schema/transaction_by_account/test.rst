storage/libradb/src/schema/transaction_by_account/test.rs
=========================================================

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
        address in any::<AccountAddress>(),
        seq_num in any::<u64>(),
        version in any::<Version>(),
    ) {
        assert_encode_decode::<TransactionByAccountSchema>(&(address, seq_num), &version);
    }
}


