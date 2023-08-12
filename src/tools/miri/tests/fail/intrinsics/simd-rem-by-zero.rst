src/tools/miri/tests/fail/intrinsics/simd-rem-by-zero.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(platform_intrinsics, repr_simd)]

extern "platform-intrinsic" {
    pub(crate) fn simd_rem<T>(x: T, y: T) -> T;
}

#[repr(simd)]
#[allow(non_camel_case_types)]
struct i32x2(i32, i32);

fn main() {
    unsafe {
        let x = i32x2(1, 1);
        let y = i32x2(1, 0);
        simd_rem(x, y); //~ERROR: Undefined Behavior: calculating the remainder with a divisor of zero
    }
}


