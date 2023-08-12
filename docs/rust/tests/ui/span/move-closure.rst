tests/ui/span/move-closure.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #24986
// Make sure that the span of a closure marked `move` begins at the `move` keyword.

fn main() {
    let x: () = move || (); //~ ERROR mismatched types
}


