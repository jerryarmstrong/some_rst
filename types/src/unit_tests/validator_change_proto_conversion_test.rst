types/src/unit_tests/validator_change_proto_conversion_test.rs
==============================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::validator_change::ValidatorChangeEventWithProof;
use proptest::prelude::*;
use solana_libra_crypto::ed25519::*;
use solana_libra_prost_ext::test_helpers::assert_protobuf_encode_decode;

proptest! {
    #![proptest_config(ProptestConfig::with_cases(20))]

    #[test]
    fn test_validator_change_event_with_proof_conversion(
        change in any::<ValidatorChangeEventWithProof<Ed25519Signature>>()
    ) {
        assert_protobuf_encode_decode::<crate::proto::types::ValidatorChangeEventWithProof, ValidatorChangeEventWithProof<_>>(&change);
    }
}


