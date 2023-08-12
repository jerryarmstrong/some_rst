tests/ui/nll/promotable-mutable-zst-doesnt-conflict.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that mutable promoted length zero arrays don't check for conflicting
// access

// check-pass

pub fn main() {
    let mut x: Vec<&[i32; 0]> = Vec::new();
    for _ in 0..10 {
        x.push(&[]);
    }
}


