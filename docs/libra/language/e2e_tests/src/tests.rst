language/e2e_tests/src/tests.rs
===============================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Test module.
//!
//! Add new test modules to this list.
//!
//! This is not in a top-level tests directory because each file there gets compiled into a
//! separate binary. The linker ends up repeating a lot of work for each binary to not much
//! benefit.

mod account_universe;
mod arithmetic;
mod create_account;
mod function_call;
mod genesis;
mod mint;
mod module_publishing;
mod pack_unpack;
mod peer_to_peer;
mod rotate_key;
mod verify_txn;


