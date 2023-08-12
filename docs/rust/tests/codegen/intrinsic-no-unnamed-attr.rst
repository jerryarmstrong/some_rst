tests/codegen/intrinsic-no-unnamed-attr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C no-prepopulate-passes

#![feature(intrinsics)]

extern "rust-intrinsic" {
    fn sqrtf32(x: f32) -> f32;
}
// CHECK: @llvm.sqrt.f32(float) #{{[0-9]*}}

fn main() {
    unsafe { sqrtf32(0.0f32); }
}


