compiler/rustc_target/src/spec/linux_gnu_base.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::TargetOptions;

pub fn opts() -> TargetOptions {
    TargetOptions { env: "gnu".into(), ..super::linux_base::opts() }
}


