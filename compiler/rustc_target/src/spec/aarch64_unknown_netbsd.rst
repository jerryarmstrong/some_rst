compiler/rustc_target/src/spec/aarch64_unknown_netbsd.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{Target, TargetOptions};

pub fn target() -> Target {
    Target {
        llvm_target: "aarch64-unknown-netbsd".into(),
        pointer_width: 64,
        data_layout: "e-m:e-i8:8:32-i16:16:32-i64:64-i128:128-n32:64-S128".into(),
        arch: "aarch64".into(),
        options: TargetOptions {
            mcount: "__mcount".into(),
            max_atomic_width: Some(128),
            ..super::netbsd_base::opts()
        },
    }
}


