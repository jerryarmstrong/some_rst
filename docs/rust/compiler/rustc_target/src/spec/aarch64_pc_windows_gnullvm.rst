compiler/rustc_target/src/spec/aarch64_pc_windows_gnullvm.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;

pub fn target() -> Target {
    let mut base = super::windows_gnullvm_base::opts();
    base.max_atomic_width = Some(128);
    base.features = "+neon,+fp-armv8".into();
    base.linker = Some("aarch64-w64-mingw32-clang".into());

    Target {
        llvm_target: "aarch64-pc-windows-gnu".into(),
        pointer_width: 64,
        data_layout: "e-m:w-p:64:64-i32:32-i64:64-i128:128-n32:64-S128".into(),
        arch: "aarch64".into(),
        options: base,
    }
}


