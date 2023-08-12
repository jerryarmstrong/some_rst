compiler/rustc_target/src/spec/bpfel_unknown_unknown.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;
use crate::spec::sbf_base;

pub fn target() -> Target {
    Target {
        llvm_target: "bpfel".into(),
        pointer_width: 64,
        arch: "bpf".into(),
        data_layout: "e-m:e-p:64:64-i64:64-n32:64-S128".into(),
        options: sbf_base::opts(),
    }
}


