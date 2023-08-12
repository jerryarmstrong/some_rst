compiler/rustc_target/src/spec/aarch64_kmc_solid_asp3.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::{RelocModel, Target, TargetOptions};

pub fn target() -> Target {
    let base = super::solid_base::opts("asp3");
    Target {
        llvm_target: "aarch64-unknown-none".into(),
        pointer_width: 64,
        data_layout: "e-m:e-i8:8:32-i16:16:32-i64:64-i128:128-n32:64-S128".into(),
        arch: "aarch64".into(),
        options: TargetOptions {
            linker: Some("aarch64-kmc-elf-gcc".into()),
            features: "+neon,+fp-armv8".into(),
            relocation_model: RelocModel::Static,
            disable_redzone: true,
            max_atomic_width: Some(128),
            ..base
        },
    }
}


