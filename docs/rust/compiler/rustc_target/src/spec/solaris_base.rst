compiler/rustc_target/src/spec/solaris_base.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{cvs, Cc, LinkerFlavor, TargetOptions};

pub fn opts() -> TargetOptions {
    TargetOptions {
        os: "solaris".into(),
        dynamic_linking: true,
        has_rpath: true,
        families: cvs!["unix"],
        is_like_solaris: true,
        linker_flavor: LinkerFlavor::Unix(Cc::Yes),
        limit_rdylib_exports: false, // Linker doesn't support this
        eh_frame_header: false,

        ..Default::default()
    }
}


