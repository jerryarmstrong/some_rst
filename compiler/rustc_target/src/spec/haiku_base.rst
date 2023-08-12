compiler/rustc_target/src/spec/haiku_base.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{cvs, RelroLevel, TargetOptions};

pub fn opts() -> TargetOptions {
    TargetOptions {
        os: "haiku".into(),
        dynamic_linking: true,
        families: cvs!["unix"],
        relro_level: RelroLevel::Full,
        ..Default::default()
    }
}


