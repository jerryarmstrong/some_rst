src/tools/clippy/tests/ui/out_of_bounds_indexing/issue-3102.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::out_of_bounds_indexing)]
#![allow(clippy::no_effect)]

fn main() {
    let x = [1, 2, 3, 4];

    // issue 3102
    let num = 1;
    &x[num..10]; // should trigger out of bounds error
    &x[10..num]; // should trigger out of bounds error
}


