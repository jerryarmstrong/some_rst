src/tools/miri/tests/fail/intrinsics/unchecked_div1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]
fn main() {
    // MIN/-1 cannot be represented
    unsafe {
        std::intrinsics::unchecked_div(i16::MIN, -1); //~ ERROR: overflow in signed division (dividing MIN by -1)
    }
}


