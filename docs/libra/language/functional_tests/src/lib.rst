language/functional_tests/src/lib.rs
====================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

#[macro_use]
extern crate lazy_static;

pub mod checker;
pub mod config;
pub mod errors;
pub mod evaluator;
mod genesis_accounts;
pub mod utils;

#[cfg(test)]
pub mod tests;


