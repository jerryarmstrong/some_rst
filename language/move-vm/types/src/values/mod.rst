language/move-vm/types/src/values/mod.rs
========================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

pub mod values_impl;

#[cfg(test)]
mod value_tests;

#[cfg(all(test, feature = "fuzzing"))]
mod value_prop_tests;

pub use values_impl::*;


