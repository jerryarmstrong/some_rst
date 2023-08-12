types/src/unit_tests/validator_set_test.rs
==========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::validator_set::ValidatorSet;
use proptest::prelude::*;
use solana_libra_canonical_serialization::test_helper::assert_canonical_encode_decode;
use solana_libra_prost_ext::test_helpers::assert_protobuf_encode_decode;

proptest! {
    #![proptest_config(ProptestConfig::with_cases(20))]

    #[test]
    fn test_validator_set_protobuf_conversion(set in any::<ValidatorSet>()) {
        assert_protobuf_encode_decode::<crate::proto::types::ValidatorSet, ValidatorSet>(&set);
    }

    #[test]
    fn test_validator_set_canonical_serialization(set in any::<ValidatorSet>()) {
        assert_canonical_encode_decode(&set);
    }
}


