types/src/unit_tests/contract_event_proto_conversion_test.rs
============================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::contract_event::{ContractEvent, EventWithProof};
use proptest::prelude::*;
use solana_libra_prost_ext::test_helpers::assert_protobuf_encode_decode;

proptest! {
    #[test]
    fn test_event(event in any::<ContractEvent>()) {
        assert_protobuf_encode_decode::<crate::proto::types::Event, ContractEvent>(&event);
    }

    #[test]
    fn test_event_with_proof(event_with_proof in any::<EventWithProof>()) {
        assert_protobuf_encode_decode::<crate::proto::types::EventWithProof, EventWithProof>(&event_with_proof);
    }
}


