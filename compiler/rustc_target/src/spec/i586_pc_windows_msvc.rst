compiler/rustc_target/src/spec/i586_pc_windows_msvc.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;

pub fn target() -> Target {
    let mut base = super::i686_pc_windows_msvc::target();
    base.cpu = "pentium".into();
    base.llvm_target = "i586-pc-windows-msvc".into();
    base
}


