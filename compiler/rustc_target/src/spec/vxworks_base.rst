compiler/rustc_target/src/spec/vxworks_base.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{cvs, TargetOptions};

pub fn opts() -> TargetOptions {
    TargetOptions {
        os: "vxworks".into(),
        env: "gnu".into(),
        vendor: "wrs".into(),
        linker: Some("wr-c++".into()),
        exe_suffix: ".vxe".into(),
        dynamic_linking: true,
        families: cvs!["unix"],
        has_rpath: true,
        has_thread_local: true,
        crt_static_default: true,
        crt_static_respected: true,
        crt_static_allows_dylibs: true,
        // VxWorks needs to implement this to support profiling
        mcount: "_mcount".into(),
        ..Default::default()
    }
}


