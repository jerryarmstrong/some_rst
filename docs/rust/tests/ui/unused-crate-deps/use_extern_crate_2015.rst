tests/ui/unused-crate-deps/use_extern_crate_2015.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Suppress by using crate

// edition:2015
// check-pass
// aux-crate:bar=bar.rs

#![warn(unused_crate_dependencies)]

extern crate bar;

fn main() {
    println!("bar {}", bar::BAR);
}


