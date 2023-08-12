language/bytecode_verifier/bytecode_verifier_tests/src/unit_tests/resources_tests.rs
====================================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use proptest::prelude::*;
use solana_libra_bytecode_verifier::ResourceTransitiveChecker;
use solana_libra_vm::file_format::CompiledModule;

proptest! {
    #[test]
    fn valid_resource_transitivity(module in CompiledModule::valid_strategy(20)) {
        let resource_checker = ResourceTransitiveChecker::new(&module);
        prop_assert!(resource_checker.verify().is_empty());
    }
}


