tests/ui/on-unimplemented/slice-index.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test new Index error message for slices

use std::ops::Index;


fn main() {
    let x = &[1, 2, 3] as &[i32];
    x[1i32]; //~ ERROR E0277
    x[..1i32]; //~ ERROR E0277
}


