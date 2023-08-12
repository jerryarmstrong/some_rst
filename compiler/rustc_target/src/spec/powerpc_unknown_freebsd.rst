compiler/rustc_target/src/spec/powerpc_unknown_freebsd.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::abi::Endian;
use crate::spec::{Cc, LinkerFlavor, Lld, StackProbeType, Target, TargetOptions};

pub fn target() -> Target {
    let mut base = super::freebsd_base::opts();
    // Extra hint to linker that we are generating secure-PLT code.
    base.add_pre_link_args(
        LinkerFlavor::Gnu(Cc::Yes, Lld::No),
        &["-m32", "--target=powerpc-unknown-freebsd13.0"],
    );
    base.max_atomic_width = Some(32);
    base.stack_probes = StackProbeType::Inline;

    Target {
        llvm_target: "powerpc-unknown-freebsd13.0".into(),
        pointer_width: 32,
        data_layout: "E-m:e-p:32:32-i64:64-n32".into(),
        arch: "powerpc".into(),
        options: TargetOptions {
            endian: Endian::Big,
            features: "+secure-plt".into(),
            mcount: "_mcount".into(),
            ..base
        },
    }
}


