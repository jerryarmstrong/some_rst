tests/ui/uninhabited/uninhabited-enum-cast.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

enum E {}

fn f(e: E) {
    println!("{}", (e as isize).to_string());
}

fn main() {}


