compiler/rustc_target/src/spec/thumbv7a_uwp_windows_msvc.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{PanicStrategy, Target, TargetOptions};

pub fn target() -> Target {
    Target {
        llvm_target: "thumbv7a-pc-windows-msvc".into(),
        pointer_width: 32,
        data_layout: "e-m:w-p:32:32-Fi8-i64:64-v128:64:128-a:0:32-n32-S64".into(),
        arch: "arm".into(),
        options: TargetOptions {
            features: "+vfp3,+neon".into(),
            max_atomic_width: Some(64),
            // FIXME(jordanrh): use PanicStrategy::Unwind when SEH is
            // implemented for windows/arm in LLVM
            panic_strategy: PanicStrategy::Abort,
            ..super::windows_uwp_msvc_base::opts()
        },
    }
}


