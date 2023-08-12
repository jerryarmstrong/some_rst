language/move-bytecode-verifier/bytecode-verifier-tests/src/unit_tests/struct_defs_tests.rs
===========================================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use move_binary_format::file_format::CompiledModule;
use move_bytecode_verifier::RecursiveStructDefChecker;
use proptest::prelude::*;

proptest! {
    #[test]
    fn valid_recursive_struct_defs(module in CompiledModule::valid_strategy(20)) {
        prop_assert!(RecursiveStructDefChecker::verify_module(&module).is_ok());
    }
}


