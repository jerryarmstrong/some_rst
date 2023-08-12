src/tools/miri/tests/pass/enum_discriminant_ptr_value.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // A niche-optimized enum where the discriminant is a pointer value -- relies on ptr-to-int casts in
// the niche handling code.
//@compile-flags: -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

fn main() {
    let x = 42;
    let val: Option<&i32> = unsafe { std::mem::transmute((&x as *const i32).wrapping_offset(2)) };
    assert!(val.is_some());
}


