compiler/rustc_target/src/spec/nto_qnx_base.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{cvs, RelroLevel, TargetOptions};

pub fn opts() -> TargetOptions {
    TargetOptions {
        crt_static_respected: true,
        dynamic_linking: true,
        env: "nto71".into(),
        executables: true,
        families: cvs!["unix"],
        has_rpath: true,
        has_thread_local: false,
        linker: Some("qcc".into()),
        os: "nto".into(),
        position_independent_executables: true,
        static_position_independent_executables: true,
        relro_level: RelroLevel::Full,
        ..Default::default()
    }
}


