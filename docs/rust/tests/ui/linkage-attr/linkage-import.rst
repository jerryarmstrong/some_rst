tests/ui/linkage-attr/linkage-import.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// aux-build:def_external.rs

extern crate def_external as dep;

fn main() {
    println!("{:p}", &dep::EXTERN);
}


