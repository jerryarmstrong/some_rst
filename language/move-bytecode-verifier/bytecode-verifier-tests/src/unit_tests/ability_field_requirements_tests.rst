language/move-bytecode-verifier/bytecode-verifier-tests/src/unit_tests/ability_field_requirements_tests.rs
==========================================================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use move_binary_format::file_format::CompiledModule;
use move_bytecode_verifier::ability_field_requirements;
use proptest::prelude::*;

proptest! {
    #[test]
    fn valid_ability_transitivity(module in CompiledModule::valid_strategy(20)) {
        prop_assert!(ability_field_requirements::verify_module(&module).is_ok());
    }
}


