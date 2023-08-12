tests/ui/array-slice-vec/bounds-check-no-overflow.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:index out of bounds
// ignore-emscripten no processes

use std::mem::size_of;

fn main() {
    let xs = [1, 2, 3];
    xs[usize::MAX / size_of::<isize>() + 1];
}


