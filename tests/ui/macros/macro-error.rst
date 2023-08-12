tests/ui/macros/macro-error.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    ($a:expr) => a; //~ ERROR macro rhs must be delimited
}

fn main() {
    foo!(0); // Check that we report errors at macro definition, not expansion.

    let _: cfg!(foo) = (); //~ ERROR non-type macro in type position
}


