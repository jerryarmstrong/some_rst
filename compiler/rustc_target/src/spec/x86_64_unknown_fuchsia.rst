compiler/rustc_target/src/spec/x86_64_unknown_fuchsia.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{SanitizerSet, StackProbeType, Target};

pub fn target() -> Target {
    let mut base = super::fuchsia_base::opts();
    base.cpu = "x86-64".into();
    base.max_atomic_width = Some(64);
    base.stack_probes = StackProbeType::X86;
    base.supported_sanitizers = SanitizerSet::ADDRESS | SanitizerSet::CFI;

    Target {
        llvm_target: "x86_64-unknown-fuchsia".into(),
        pointer_width: 64,
        data_layout: "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
            .into(),
        arch: "x86_64".into(),
        options: base,
    }
}


