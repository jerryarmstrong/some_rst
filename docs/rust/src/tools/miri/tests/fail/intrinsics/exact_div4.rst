src/tools/miri/tests/fail/intrinsics/exact_div4.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
fn main() {
    // divison of MIN by -1
    unsafe { std::intrinsics::exact_div(i64::MIN, -1) }; //~ ERROR: overflow in signed remainder (dividing MIN by -1)
}


