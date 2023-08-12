tests/ui/numbers-arithmetic/u8-incr.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




pub fn main() {
    let mut x: u8 = 12;
    let y: u8 = 12;
    x = x + 1;
    x = x - 1;
    assert_eq!(x, y);
    // x = 14;
    // x = x + 1;

}


