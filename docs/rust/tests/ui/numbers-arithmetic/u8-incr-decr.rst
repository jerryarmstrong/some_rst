tests/ui/numbers-arithmetic/u8-incr-decr.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




// These constants were chosen because they aren't used anywhere
// in the rest of the generated code so they're easily grep-able.

pub fn main() {
    let mut x: u8 = 19; // 0x13

    let mut y: u8 = 35; // 0x23

    x = x + 7; // 0x7

    y = y - 9; // 0x9

    assert_eq!(x, y);
}


