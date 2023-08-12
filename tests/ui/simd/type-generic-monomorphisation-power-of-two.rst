tests/ui/simd/type-generic-monomorphisation-power-of-two.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(repr_simd, platform_intrinsics)]

#[repr(simd)]
struct Simd<const N: usize>([f32; N]);

fn main() {
    let _ = Simd::<3>([0.; 3]);
}


