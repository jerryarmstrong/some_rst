src/tools/miri/tests/fail/invalid_char.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Validation makes this fail in the wrong place
// Make sure we find these even with many checks disabled.
//@compile-flags: -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

fn main() {
    let c = 0xFFFFFFu32;
    assert!(std::char::from_u32(c).is_none());
    let c = unsafe { std::mem::transmute::<u32, char>(c) };
    let _x = c == 'x'; //~ ERROR: interpreting an invalid 32-bit value as a char
}


