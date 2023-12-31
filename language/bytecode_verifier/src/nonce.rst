language/bytecode_verifier/src/nonce.rs
=======================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module implements the Nonce type used for borrow checking in the abstract interpreter.
//! A Nonce instance represents an arbitrary reference or access path.
//! The integer inside a Nonce is meaningless; only equality and borrow relationships are
//! meaningful.
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq, Ord, PartialOrd)]
pub struct Nonce(usize);

impl Nonce {
    pub fn new(n: usize) -> Self {
        Self(n)
    }

    pub fn is(&self, n: usize) -> bool {
        self.0 == n
    }

    pub fn inner(&self) -> usize {
        self.0
    }
}


