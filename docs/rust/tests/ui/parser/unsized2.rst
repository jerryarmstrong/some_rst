tests/ui/parser/unsized2.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test syntax checks for `type` keyword.

fn f<X>() {}

pub fn main() {
    f<type>(); //~ ERROR expected expression, found keyword `type`
}


