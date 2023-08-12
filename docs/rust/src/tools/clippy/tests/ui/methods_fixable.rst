src/tools/clippy/tests/ui/methods_fixable.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::filter_next)]

/// Checks implementation of `FILTER_NEXT` lint.
fn main() {
    let v = vec![3, 2, 1, 0, -1, -2, -3];

    // Single-line case.
    let _ = v.iter().filter(|&x| *x < 0).next();
}


