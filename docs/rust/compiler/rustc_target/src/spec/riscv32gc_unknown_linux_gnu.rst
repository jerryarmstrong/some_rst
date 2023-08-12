compiler/rustc_target/src/spec/riscv32gc_unknown_linux_gnu.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{CodeModel, Target, TargetOptions};

pub fn target() -> Target {
    Target {
        llvm_target: "riscv32-unknown-linux-gnu".into(),
        pointer_width: 32,
        data_layout: "e-m:e-p:32:32-i64:64-n32-S128".into(),
        arch: "riscv32".into(),
        options: TargetOptions {
            code_model: Some(CodeModel::Medium),
            cpu: "generic-rv32".into(),
            features: "+m,+a,+f,+d,+c".into(),
            llvm_abiname: "ilp32d".into(),
            max_atomic_width: Some(32),
            ..super::linux_gnu_base::opts()
        },
    }
}


