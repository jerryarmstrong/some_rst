tests/ui/missing/missing-items/missing-type-parameter.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<X>() { }

fn main() {
    foo(); //~ ERROR type annotations needed
}


