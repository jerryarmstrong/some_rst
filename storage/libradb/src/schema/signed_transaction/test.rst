storage/libradb/src/schema/signed_transaction/test.rs
=====================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use proptest::prelude::*;
use solana_libra_schemadb::schema::assert_encode_decode;
use solana_libra_types::transaction::SignedTransaction;

proptest! {
    #[test]
    fn test_encode_decode(txn in any::<SignedTransaction>()) {
        assert_encode_decode::<SignedTransactionSchema>(&0u64, &txn);
    }
}


