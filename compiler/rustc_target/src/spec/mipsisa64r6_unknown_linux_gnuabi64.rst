compiler/rustc_target/src/spec/mipsisa64r6_unknown_linux_gnuabi64.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::abi::Endian;
use crate::spec::{Target, TargetOptions};

pub fn target() -> Target {
    Target {
        llvm_target: "mipsisa64r6-unknown-linux-gnuabi64".into(),
        pointer_width: 64,
        data_layout: "E-m:e-i8:8:32-i16:16:32-i64:64-n32:64-S128".into(),
        arch: "mips64".into(),
        options: TargetOptions {
            abi: "abi64".into(),
            endian: Endian::Big,
            // NOTE(mips64r6) matches C toolchain
            cpu: "mips64r6".into(),
            features: "+mips64r6".into(),
            max_atomic_width: Some(64),
            mcount: "_mcount".into(),

            ..super::linux_gnu_base::opts()
        },
    }
}


