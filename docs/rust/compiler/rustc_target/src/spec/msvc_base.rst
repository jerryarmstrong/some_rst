compiler/rustc_target/src/spec/msvc_base.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{DebuginfoKind, LinkerFlavor, Lld, SplitDebuginfo, TargetOptions};
use std::borrow::Cow;

pub fn opts() -> TargetOptions {
    // Suppress the verbose logo and authorship debugging output, which would needlessly
    // clog any log files.
    let pre_link_args = TargetOptions::link_args(LinkerFlavor::Msvc(Lld::No), &["/NOLOGO"]);

    TargetOptions {
        linker_flavor: LinkerFlavor::Msvc(Lld::No),
        is_like_windows: true,
        is_like_msvc: true,
        pre_link_args,
        abi_return_struct_as_int: true,
        emit_debug_gdb_scripts: false,

        // Currently this is the only supported method of debuginfo on MSVC
        // where `*.pdb` files show up next to the final artifact.
        split_debuginfo: SplitDebuginfo::Packed,
        supported_split_debuginfo: Cow::Borrowed(&[SplitDebuginfo::Packed]),
        debuginfo_kind: DebuginfoKind::Pdb,

        ..Default::default()
    }
}


