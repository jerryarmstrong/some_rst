language/bytecode_verifier/src/lib.rs
=====================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Verifies bytecode sanity.

// Bounds checks are implemented in the `vm` crate.
pub mod absint;
pub mod abstract_state;
pub mod acquires_list_verifier;
pub mod check_duplication;
pub mod code_unit_verifier;
pub mod control_flow_graph;
pub mod instantiation_loops;
pub mod nonce;
pub mod partition;
pub mod resources;
pub mod signature;
pub mod stack_usage_verifier;
pub mod struct_defs;
pub mod type_memory_safety;
pub mod unused_entries;

pub mod verifier;

pub use check_duplication::DuplicationChecker;
pub use code_unit_verifier::CodeUnitVerifier;
pub use resources::ResourceTransitiveChecker;
pub use signature::SignatureChecker;
pub use stack_usage_verifier::StackUsageVerifier;
pub use struct_defs::RecursiveStructDefChecker;
pub use unused_entries::UnusedEntryChecker;
pub use verifier::{
    verify_main_signature, verify_module_dependencies, verify_script_dependencies, VerifiedModule,
    VerifiedScript,
};


