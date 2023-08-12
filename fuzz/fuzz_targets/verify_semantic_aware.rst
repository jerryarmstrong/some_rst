fuzz/fuzz_targets/verify_semantic_aware.rs
==========================================

Last edited: 2023-08-10 08:46:13

Contents:

.. code-block:: rs

    #![no_main]

use libfuzzer_sys::fuzz_target;

use semantic_aware::*;
use solana_rbpf::{
    elf::{FunctionRegistry, SBPFVersion},
    insn_builder::IntoBytes,
    verifier::{RequisiteVerifier, Verifier},
};

use crate::common::ConfigTemplate;

mod common;
mod semantic_aware;

#[derive(arbitrary::Arbitrary, Debug)]
struct FuzzData {
    template: ConfigTemplate,
    prog: FuzzProgram,
}

fuzz_target!(|data: FuzzData| {
    let prog = make_program(&data.prog);
    let config = data.template.into();
    let function_registry = FunctionRegistry::default();
    RequisiteVerifier::verify(prog.into_bytes(), &config, &SBPFVersion::V2, &function_registry).unwrap();
});


