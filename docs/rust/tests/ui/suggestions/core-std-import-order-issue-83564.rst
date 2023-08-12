tests/ui/suggestions/core-std-import-order-issue-83564.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// This is a regression test for #83564.
// For some reason, Rust 2018 or higher is required to reproduce the bug.

fn main() {
    //~^ HELP consider importing one of these items
    let _x = NonZeroU32::new(5).unwrap();
    //~^ ERROR failed to resolve: use of undeclared type `NonZeroU32`
}


