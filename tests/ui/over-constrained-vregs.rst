tests/ui/over-constrained-vregs.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_must_use)]
// Regression test for issue #152.
pub fn main() {
    let mut b: usize = 1_usize;
    while b < std::mem::size_of::<usize>() {
        0_usize << b;
        b <<= 1_usize;
        println!("{}", b);
    }
}


