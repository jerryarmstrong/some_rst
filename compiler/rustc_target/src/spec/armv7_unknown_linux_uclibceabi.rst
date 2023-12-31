compiler/rustc_target/src/spec/armv7_unknown_linux_uclibceabi.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{Target, TargetOptions};

// This target is for uclibc Linux on ARMv7 without NEON,
// thumb-mode or hardfloat.

pub fn target() -> Target {
    let base = super::linux_uclibc_base::opts();
    Target {
        llvm_target: "armv7-unknown-linux-gnueabi".into(),
        pointer_width: 32,
        data_layout: "e-m:e-p:32:32-Fi8-i64:64-v128:64:128-a:0:32-n32-S64".into(),
        arch: "arm".into(),

        options: TargetOptions {
            features: "+v7,+thumb2,+soft-float,-neon".into(),
            cpu: "generic".into(),
            max_atomic_width: Some(64),
            mcount: "_mcount".into(),
            abi: "eabi".into(),
            ..base
        },
    }
}


