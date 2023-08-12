tests/ui/numbers-arithmetic/i8-incr.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




pub fn main() {
    let mut x: i8 = -12;
    let y: i8 = -12;
    x = x + 1;
    x = x - 1;
    assert_eq!(x, y);
}


