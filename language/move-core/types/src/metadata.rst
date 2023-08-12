language/move-core/types/src/metadata.rs
========================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

/// Representation of metadata,
#[derive(Clone, PartialEq, Eq, Debug)]
#[cfg_attr(feature = "fuzzing", derive(arbitrary::Arbitrary))]
pub struct Metadata {
    /// The key identifying the type of metadata.
    pub key: Vec<u8>,
    /// The value of the metadata.
    pub value: Vec<u8>,
}


