tests/ui/simd/type-generic-monomorphisation-oversized.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

#![feature(repr_simd, platform_intrinsics)]

// error-pattern:monomorphising SIMD type `Simd<65536>` of length greater than 32768

#[repr(simd)]
struct Simd<const N: usize>([f32; N]);

fn main() {
    let _ = Simd::<65536>([0.; 65536]);
}


