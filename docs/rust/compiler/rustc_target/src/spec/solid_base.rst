compiler/rustc_target/src/spec/solid_base.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::FramePointer;
use crate::spec::TargetOptions;

pub fn opts(kernel: &str) -> TargetOptions {
    TargetOptions {
        os: format!("solid_{kernel}").into(),
        vendor: "kmc".into(),
        executables: false,
        frame_pointer: FramePointer::NonLeaf,
        has_thread_local: true,
        ..Default::default()
    }
}


