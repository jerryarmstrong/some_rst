tests/ui/consts/const-tup-index-span.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test spans of errors

const TUP: (usize,) = 5usize << 64;
//~^ ERROR mismatched types
//~| expected tuple, found `usize`
const ARR: [i32; TUP.0] = [];
//~^ constant

fn main() {
}


