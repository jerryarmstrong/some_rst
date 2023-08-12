tests/ui/underscore-imports/duplicate.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:duplicate.rs

extern crate duplicate;

#[duplicate::duplicate]
use main as _; // OK

macro_rules! duplicate {
    ($item: item) => { $item $item }
}

duplicate!(use std as _;); // OK

fn main() {}


