language/move-bytecode-verifier/fuzz/fuzz_targets/compiled_module.rs
====================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

#![no_main]
use libfuzzer_sys::fuzz_target;
use move_binary_format::file_format::CompiledModule;

fuzz_target!(|module: CompiledModule| {
    let _ = move_bytecode_verifier::verify_module(&module);
});


