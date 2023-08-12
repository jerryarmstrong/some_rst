tests/ui/consts/const-const.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

const a: isize = 1;
const b: isize = a + 2;

pub fn main() {
    assert_eq!(b, 3);
}


