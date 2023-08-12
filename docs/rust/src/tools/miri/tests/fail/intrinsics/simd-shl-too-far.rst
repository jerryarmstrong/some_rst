src/tools/miri/tests/fail/intrinsics/simd-shl-too-far.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(platform_intrinsics, repr_simd)]

extern "platform-intrinsic" {
    pub(crate) fn simd_shl<T>(x: T, y: T) -> T;
}

#[repr(simd)]
#[allow(non_camel_case_types)]
struct i32x2(i32, i32);

fn main() {
    unsafe {
        let x = i32x2(1, 1);
        let y = i32x2(100, 0);
        simd_shl(x, y); //~ERROR: overflowing shift by 100 in `simd_shl` in SIMD lane 0
    }
}


