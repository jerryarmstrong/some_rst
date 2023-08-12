src/tools/miri/tests/fail/intrinsics/simd-reduce-invalid-bool.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(platform_intrinsics, repr_simd)]

extern "platform-intrinsic" {
    pub(crate) fn simd_reduce_any<T>(x: T) -> bool;
}

#[repr(simd)]
#[allow(non_camel_case_types)]
struct i32x2(i32, i32);

fn main() {
    unsafe {
        let x = i32x2(0, 1);
        simd_reduce_any(x); //~ERROR: must be all-0-bits or all-1-bits
    }
}


