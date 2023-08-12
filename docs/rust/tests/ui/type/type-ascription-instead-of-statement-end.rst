tests/ui/type/type-ascription-instead-of-statement-end.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_ascription)]

fn main() {
    println!("test"):
    0; //~ ERROR expected type, found `0`
}

fn foo() {
    println!("test"): 0; //~ ERROR expected type, found `0`
}


