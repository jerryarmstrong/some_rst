tests/pretty/empty-lines.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib

// Issue #759
// Whitespace under block opening should not expand forever

fn a() -> usize {

    1
}


