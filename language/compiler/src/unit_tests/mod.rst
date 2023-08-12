language/compiler/src/unit_tests/mod.rs
=======================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

// Needs to be at the top to allow macros defined in here to be used in tests.
#[macro_use]
pub(crate) mod testutils;

mod branch_tests;
mod cfg_tests;
mod expression_tests;
mod function_tests;
mod import_tests;
mod serializer_tests;
mod stdlib_scripts;


