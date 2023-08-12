src/tools/miri/tests/fail/intrinsics/exact_div2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
fn main() {
    // divison with a remainder
    unsafe { std::intrinsics::exact_div(2u16, 3) }; //~ ERROR: 2_u16 cannot be divided by 3_u16 without remainder
}


