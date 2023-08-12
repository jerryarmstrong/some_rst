language/move-ir-compiler/src/unit_tests/mod.rs
===============================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

// Needs to be at the top to allow macros defined in here to be used in tests.
#[macro_use]
pub(crate) mod testutils;

mod cfg_tests;
mod function_tests;


