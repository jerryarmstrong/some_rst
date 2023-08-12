tests/ui/array-slice-vec/nested-vec-1.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Test that using the `vec!` macro nested within itself works

fn main() {
    let nested = vec![vec![1u32, 2u32, 3u32]];
    assert_eq!(nested[0][1], 2);
}


