compiler/rustc_target/src/spec/mipsel_unknown_linux_gnu.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{Target, TargetOptions};

pub fn target() -> Target {
    Target {
        llvm_target: "mipsel-unknown-linux-gnu".into(),
        pointer_width: 32,
        data_layout: "e-m:m-p:32:32-i8:8:32-i16:16:32-i64:64-n32-S64".into(),
        arch: "mips".into(),

        options: TargetOptions {
            cpu: "mips32r2".into(),
            features: "+mips32r2,+fpxx,+nooddspreg".into(),
            max_atomic_width: Some(32),
            mcount: "_mcount".into(),

            ..super::linux_gnu_base::opts()
        },
    }
}


