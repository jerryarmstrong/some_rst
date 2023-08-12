src/tools/miri/tests/fail/intrinsics/exact_div3.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
fn main() {
    // signed divison with a remainder
    unsafe { std::intrinsics::exact_div(-19i8, 2) }; //~ ERROR: -19_i8 cannot be divided by 2_i8 without remainder
}


