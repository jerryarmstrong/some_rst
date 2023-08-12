language/tools/cost-synthesis/src/natives.rs
============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Logic for generating valid stack states for native function calls.
//!
//! This implements a `StackAccessor` that generates random bytearrays of a user defined length. We
//! then use this ability to run the native functions with different bytearray lengths in the
//! generated synthesis binary.
use rand::{rngs::StdRng, Rng, SeedableRng};
use solana_libra_types::byte_array::ByteArray;

/// A wrapper around data used to generate random valid bytearrays
pub struct StackAccessorMocker {
    gen: StdRng,
    /// The length of bytearrays that will be generated.
    pub hash_length: usize,
}

impl StackAccessorMocker {
    /// Builds a new stack accessor mocker. User is responsible for later setting the length of,
    /// and generating the underlying bytearray.
    pub fn new() -> Self {
        let seed: [u8; 32] = [0; 32];
        Self {
            gen: StdRng::from_seed(seed),
            hash_length: 1,
        }
    }

    /// Set the bytearray length that will be generated in calls to `next_bytearray`.
    pub fn set_hash_length(&mut self, len: usize) {
        self.hash_length = len;
    }

    /// Generage a fresh bytearray.
    pub fn next_bytearray(&mut self) -> ByteArray {
        let bytes: Vec<u8> = (0..self.hash_length)
            .map(|_| self.gen.gen::<u8>())
            .collect();
        ByteArray::new(bytes)
    }
}

impl Default for StackAccessorMocker {
    fn default() -> Self {
        Self::new()
    }
}


