language/functional_tests/src/genesis_accounts.rs
=================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use solana_libra_language_e2e_tests::account::Account;
use std::collections::BTreeMap;

// These are special-cased since they are generated in genesis, and therefore we don't want
// their account states to be generated.
pub const ASSOCIATION_NAME: &str = "association";

pub fn make_genesis_accounts() -> BTreeMap<String, Account> {
    let mut m = BTreeMap::new();
    m.insert(ASSOCIATION_NAME.to_string(), Account::new_association());
    m
}


