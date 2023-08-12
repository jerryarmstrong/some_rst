tests/ui/mismatched_types/similar_paths_primitive.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_camel_case_types)]

struct bool;

fn foo(_: bool) {}

fn main() {
    foo(true);
    //~^ ERROR mismatched types [E0308]
}


