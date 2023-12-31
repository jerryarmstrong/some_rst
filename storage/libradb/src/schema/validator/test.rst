storage/libradb/src/schema/validator/test.rs
============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use itertools::Itertools;
use rand::{
    rngs::{OsRng, StdRng},
    seq::SliceRandom,
    thread_rng, Rng, SeedableRng,
};
use solana_libra_crypto::ed25519::compat;
use solana_libra_schemadb::schema::assert_encode_decode;
use solana_libra_types::transaction::Version;
use std::vec::IntoIter;

fn row_with_arbitrary_validator(version: Version) -> (Key, ()) {
    let mut seed_rng = OsRng::default();
    let seed_buf: [u8; 32] = seed_rng.gen();
    let mut rng = StdRng::from_seed(seed_buf);
    let (_private_key, public_key) = compat::generate_keypair(&mut rng);
    (
        Key {
            version,
            public_key,
        },
        (),
    )
}

#[test]
fn test_encode_decode() {
    let (k, v) = row_with_arbitrary_validator(1);
    assert_encode_decode::<ValidatorSchema>(&k, &v);
}

#[test]
fn test_order() {
    let mut versions: Vec<u64> = (0..1024).collect();
    versions.shuffle(&mut thread_rng());

    let encoded_sorted: IntoIter<Vec<u8>> = versions
        .into_iter()
        .map(|v| row_with_arbitrary_validator(v).0.encode_key().unwrap())
        .sorted();

    let decoded_versions: Vec<Version> = encoded_sorted
        .map(|k| Key::decode_key(&k).unwrap().version)
        .collect();

    let ordered_versions: Vec<Version> = (0..1024).collect();

    assert_eq!(decoded_versions, ordered_versions)
}


