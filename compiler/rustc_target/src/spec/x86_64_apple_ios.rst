compiler/rustc_target/src/spec/x86_64_apple_ios.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::apple_base::{ios_sim_llvm_target, opts, Arch};
use crate::spec::{StackProbeType, Target, TargetOptions};

pub fn target() -> Target {
    let arch = Arch::X86_64_sim;
    Target {
        llvm_target: ios_sim_llvm_target(arch).into(),
        pointer_width: 64,
        data_layout: "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
            .into(),
        arch: arch.target_arch(),
        options: TargetOptions {
            max_atomic_width: Some(64),
            stack_probes: StackProbeType::X86,
            ..opts("ios", arch)
        },
    }
}


