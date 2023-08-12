compiler/rustc_target/src/spec/aarch64_uwp_windows_msvc.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;

pub fn target() -> Target {
    let mut base = super::windows_uwp_msvc_base::opts();
    base.max_atomic_width = Some(128);

    Target {
        llvm_target: "aarch64-pc-windows-msvc".into(),
        pointer_width: 64,
        data_layout: "e-m:w-p:64:64-i32:32-i64:64-i128:128-n32:64-S128".into(),
        arch: "aarch64".into(),
        options: base,
    }
}


