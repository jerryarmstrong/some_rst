tests/ui/numbers-arithmetic/signed-shift-const-eval.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]


enum test { thing = -5 >> 1_usize }
pub fn main() {
    assert_eq!(test::thing as isize, -3);
}


