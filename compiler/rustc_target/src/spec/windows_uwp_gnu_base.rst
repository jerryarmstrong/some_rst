compiler/rustc_target/src/spec/windows_uwp_gnu_base.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{Cc, LinkArgs, LinkerFlavor, Lld, TargetOptions};

pub fn opts() -> TargetOptions {
    let base = super::windows_gnu_base::opts();

    // FIXME: This should be updated for the exception machinery changes from #67502
    // and inherit from `windows_gnu_base`, at least partially.
    let mingw_libs = &[
        "-lwinstorecompat",
        "-lruntimeobject",
        "-lsynchronization",
        "-lvcruntime140_app",
        "-lucrt",
        "-lwindowsapp",
        "-lmingwex",
        "-lmingw32",
    ];
    let mut late_link_args =
        TargetOptions::link_args(LinkerFlavor::Gnu(Cc::No, Lld::No), mingw_libs);
    super::add_link_args(&mut late_link_args, LinkerFlavor::Gnu(Cc::Yes, Lld::No), mingw_libs);
    // Reset the flags back to empty until the FIXME above is addressed.
    let late_link_args_dynamic = LinkArgs::new();
    let late_link_args_static = LinkArgs::new();

    TargetOptions {
        abi: "uwp".into(),
        vendor: "uwp".into(),
        limit_rdylib_exports: false,
        late_link_args,
        late_link_args_dynamic,
        late_link_args_static,

        ..base
    }
}


