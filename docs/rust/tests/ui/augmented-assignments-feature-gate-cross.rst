tests/ui/augmented-assignments-feature-gate-cross.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:augmented_assignments.rs

extern crate augmented_assignments;

use augmented_assignments::Int;

fn main() {
    let mut x = Int(0);
    x += 1;
}


