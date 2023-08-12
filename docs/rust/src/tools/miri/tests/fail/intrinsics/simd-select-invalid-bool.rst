src/tools/miri/tests/fail/intrinsics/simd-select-invalid-bool.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(platform_intrinsics, repr_simd)]

extern "platform-intrinsic" {
    fn simd_select<M, T>(m: M, yes: T, no: T) -> T;
}

#[repr(simd)]
#[allow(non_camel_case_types)]
#[derive(Copy, Clone)]
struct i32x2(i32, i32);

fn main() {
    unsafe {
        let x = i32x2(0, 1);
        simd_select(x, x, x); //~ERROR: must be all-0-bits or all-1-bits
    }
}


