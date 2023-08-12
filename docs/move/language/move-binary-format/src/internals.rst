language/move-binary-format/src/internals.rs
============================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

//! Types meant for use by other parts of this crate, and by other crates that are designed to
//! work with the internals of these data structures.

use crate::IndexKind;

/// Represents a module index.
pub trait ModuleIndex {
    const KIND: IndexKind;

    fn into_index(self) -> usize;
}


