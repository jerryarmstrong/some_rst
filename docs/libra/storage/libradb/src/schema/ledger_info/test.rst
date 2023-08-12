storage/libradb/src/schema/ledger_info/test.rs
==============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use proptest::prelude::*;
use solana_libra_schemadb::schema::assert_encode_decode;
use solana_libra_types::crypto_proxies::LedgerInfoWithSignatures;

proptest! {
    #[test]
    fn test_encode_decode(
        ledger_info_with_sigs in any_with::<LedgerInfoWithSignatures>((1..10).into())
    ) {
        assert_encode_decode::<LedgerInfoSchema>(&0, &ledger_info_with_sigs);
    }
}


