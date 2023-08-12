src/tools/miri/tests/fail/fast_math_first.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

fn main() {
    unsafe {
        let _x: f32 = core::intrinsics::frem_fast(f32::NAN, 3.2); //~ ERROR: `frem_fast` intrinsic called with non-finite value as first parameter
    }
}


