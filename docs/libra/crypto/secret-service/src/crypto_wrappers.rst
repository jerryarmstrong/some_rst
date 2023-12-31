crypto/secret-service/src/crypto_wrappers.rs
============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module contains wrappers around nextgen crypto API to support crypto agility
//! and to make the secret service agnostic to the details of the particular signing algorithms.

use serde::{Deserialize, Serialize};
use solana_libra_crypto::{
    bls12381::{BLS12381PrivateKey, BLS12381PublicKey, BLS12381Signature},
    ed25519::{Ed25519PrivateKey, Ed25519PublicKey, Ed25519Signature},
    hash::HashValue,
};
use solana_libra_crypto_derive::{
    Deref, PrivateKey, PublicKey, Signature, SigningKey, SilentDebug, ValidKey, VerifyingKey,
};

/// KeyID value is a handler to the secret key and a simple wrapper around the hash value.
#[derive(Clone, Deref, PartialEq, Eq, Hash)]
pub struct KeyID(pub HashValue);

///////////////////////////////////////////////////////////////////
// Declarations pulled from crypto/src/unit_tests/cross_test.rs  //
///////////////////////////////////////////////////////////////////
/// Generic public key enum
#[derive(
    Serialize, Deserialize, Debug, Clone, PartialEq, Eq, Hash, ValidKey, PublicKey, VerifyingKey,
)]
#[PrivateKeyType = "GenericPrivateKey"]
#[SignatureType = "GenericSignature"]
pub enum GenericPublicKey {
    /// Ed25519 public key
    Ed(Ed25519PublicKey),
    /// BLS12-381 public key
    BLS(BLS12381PublicKey),
}

/// Generic private key enum
#[derive(Serialize, Deserialize, SilentDebug, ValidKey, PrivateKey, SigningKey)]
#[PublicKeyType = "GenericPublicKey"]
#[SignatureType = "GenericSignature"]
pub enum GenericPrivateKey {
    /// Ed25519 private key
    Ed(Ed25519PrivateKey),
    /// BLS12-381 private key
    BLS(BLS12381PrivateKey),
}

/// Generic signature enum
#[allow(clippy::large_enum_variant)]
#[derive(Clone, Debug, PartialEq, Eq, Hash, Signature)]
#[PrivateKeyType = "GenericPrivateKey"]
#[PublicKeyType = "GenericPublicKey"]
pub enum GenericSignature {
    /// Ed25519 signature
    Ed(Ed25519Signature),
    /// BLS12-381 signature
    BLS(BLS12381Signature),
}


