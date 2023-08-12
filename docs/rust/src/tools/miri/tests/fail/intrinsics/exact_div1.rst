src/tools/miri/tests/fail/intrinsics/exact_div1.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
fn main() {
    // divison by 0
    unsafe { std::intrinsics::exact_div(2, 0) }; //~ ERROR: divisor of zero
}


