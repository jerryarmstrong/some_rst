tests/ui/parser/bad-pointer-type.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_: *()) {
    //~^ ERROR expected `mut` or `const` keyword in raw pointer type
}

fn main() {}


