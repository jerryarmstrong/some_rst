compiler/rustc_target/src/spec/l4re_base.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{cvs, Cc, LinkerFlavor, PanicStrategy, RelocModel, TargetOptions};

pub fn opts() -> TargetOptions {
    TargetOptions {
        os: "l4re".into(),
        env: "uclibc".into(),
        linker_flavor: LinkerFlavor::Unix(Cc::No),
        panic_strategy: PanicStrategy::Abort,
        linker: Some("l4-bender".into()),
        families: cvs!["unix"],
        relocation_model: RelocModel::Static,
        ..Default::default()
    }
}


