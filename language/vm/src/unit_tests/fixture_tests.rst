language/vm/src/unit_tests/fixture_tests.rs
===========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::file_format::CompiledScript;
use solana_libra_types::test_helpers::transaction_test_helpers::placeholder_script;

// Ensure that the placeholder_script fixture deserializes properly, i.e. is kept up to date.
#[test]
fn placeholder_script_deserialize() {
    let placeholder_program = placeholder_script();
    CompiledScript::deserialize(&placeholder_program.code())
        .expect("script should deserialize properly");
}


