compiler/rustc_target/src/spec/bpfeb_unknown_none.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;
use crate::{abi::Endian, spec::bpf_base};

pub fn target() -> Target {
    Target {
        llvm_target: "bpfeb".into(),
        data_layout: "E-m:e-p:64:64-i64:64-i128:128-n32:64-S128".into(),
        pointer_width: 64,
        arch: "bpf".into(),
        options: bpf_base::opts(Endian::Big),
    }
}


