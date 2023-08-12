compiler/rustc_target/src/spec/aarch64_be_unknown_linux_gnu_ilp32.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::abi::Endian;
use crate::spec::{Target, TargetOptions};

pub fn target() -> Target {
    let mut base = super::linux_gnu_base::opts();
    base.max_atomic_width = Some(128);

    Target {
        llvm_target: "aarch64_be-unknown-linux-gnu_ilp32".into(),
        pointer_width: 32,
        data_layout: "E-m:e-p:32:32-i8:8:32-i16:16:32-i64:64-i128:128-n32:64-S128".into(),
        arch: "aarch64".into(),
        options: TargetOptions {
            abi: "ilp32".into(),
            features: "+outline-atomics".into(),
            mcount: "\u{1}_mcount".into(),
            endian: Endian::Big,
            ..base
        },
    }
}


