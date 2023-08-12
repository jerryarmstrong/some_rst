compiler/rustc_target/src/spec/windows_uwp_msvc_base.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{LinkerFlavor, Lld, TargetOptions};

pub fn opts() -> TargetOptions {
    let mut opts = super::windows_msvc_base::opts();

    opts.abi = "uwp".into();
    opts.vendor = "uwp".into();
    opts.add_pre_link_args(LinkerFlavor::Msvc(Lld::No), &["/APPCONTAINER", "mincore.lib"]);

    opts
}


