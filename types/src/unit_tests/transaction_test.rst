types/src/unit_tests/transaction_test.rs
========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::{
    account_address::AccountAddress,
    transaction::{RawTransaction, Script, SignedTransaction, TransactionPayload},
};
use proptest::prelude::*;
use solana_libra_canonical_serialization::{
    CanonicalDeserializer, CanonicalSerializer, SimpleDeserializer, SimpleSerializer,
};
use solana_libra_crypto::ed25519::*;
use std::convert::TryFrom;

#[test]
fn test_invalid_signature() {
    let keypair = compat::generate_keypair(None);
    let proto_txn: crate::proto::types::SignedTransaction = SignedTransaction::new(
        RawTransaction::new_script(
            AccountAddress::random(),
            0,
            Script::new(vec![], vec![]),
            0,
            0,
            std::time::Duration::new(0, 0),
        ),
        keypair.1,
        Ed25519Signature::try_from(&[1u8; 64][..]).unwrap(),
    )
    .into();
    let txn = SignedTransaction::try_from(proto_txn)
        .expect("initial conversion from_proto should succeed");
    txn.check_signature()
        .expect_err("signature checking should fail");
}

proptest! {
    #[test]
    fn test_sig(raw_txn in any::<RawTransaction>(), (sk1, pk1) in compat::keypair_strategy()) {
        let txn = raw_txn.sign(&sk1, pk1).unwrap();
        let signed_txn = txn.into_inner();
        assert!(signed_txn.check_signature().is_ok());
    }

    #[test]
    fn transaction_payload_round_trip_canonical_serialization(txn_payload in any::<TransactionPayload>()) {
        let mut serializer = SimpleSerializer::<Vec<u8>>::new();
        serializer.encode_struct(&txn_payload).unwrap();
        let serialized_bytes = serializer.get_output();

        let mut deserializer = SimpleDeserializer::new(&serialized_bytes);
        let output: TransactionPayload = deserializer.decode_struct().unwrap();
        assert_eq!(txn_payload, output);
    }

    #[test]
    fn transaction_round_trip_canonical_serialization(raw_txn in any::<RawTransaction>()) {
        let mut serializer = SimpleSerializer::<Vec<u8>>::new();
        serializer.encode_struct(&raw_txn).unwrap();
        let serialized_bytes = serializer.get_output();

        let mut deserializer = SimpleDeserializer::new(&serialized_bytes);
        let output: RawTransaction = deserializer.decode_struct().unwrap();
        assert_eq!(raw_txn, output);
    }
}


