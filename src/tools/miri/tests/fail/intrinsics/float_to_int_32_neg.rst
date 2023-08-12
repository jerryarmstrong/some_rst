src/tools/miri/tests/fail/intrinsics/float_to_int_32_neg.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

// Directly call intrinsic to avoid debug assertions in libstd
extern "rust-intrinsic" {
    fn float_to_int_unchecked<Float: Copy, Int: Copy>(value: Float) -> Int;
}

fn main() {
    unsafe {
        float_to_int_unchecked::<f32, u32>(-1.000000001f32); //~ ERROR: cannot be represented in target type `u32`
    }
}


