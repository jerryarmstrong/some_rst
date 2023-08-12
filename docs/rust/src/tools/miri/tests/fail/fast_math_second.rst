src/tools/miri/tests/fail/fast_math_second.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

fn main() {
    unsafe {
        let _x: f32 = core::intrinsics::fmul_fast(3.4f32, f32::INFINITY); //~ ERROR: `fmul_fast` intrinsic called with non-finite value as second parameter
    }
}


