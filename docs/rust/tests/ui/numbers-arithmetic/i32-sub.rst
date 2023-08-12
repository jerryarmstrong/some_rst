tests/ui/numbers-arithmetic/i32-sub.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




pub fn main() { let mut x: i32 = -400; x = 0 - x; assert_eq!(x, 400); }


