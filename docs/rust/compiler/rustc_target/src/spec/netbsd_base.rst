compiler/rustc_target/src/spec/netbsd_base.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{cvs, RelroLevel, TargetOptions};

pub fn opts() -> TargetOptions {
    TargetOptions {
        os: "netbsd".into(),
        dynamic_linking: true,
        families: cvs!["unix"],
        no_default_libraries: false,
        has_rpath: true,
        position_independent_executables: true,
        relro_level: RelroLevel::Full,
        use_ctors_section: true,
        default_dwarf_version: 2,
        ..Default::default()
    }
}


