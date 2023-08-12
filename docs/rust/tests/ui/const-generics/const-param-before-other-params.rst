tests/ui/const-generics/const-param-before-other-params.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar<const X: u8, 'a>(_: &'a ()) {
    //~^ ERROR lifetime parameters must be declared prior to type and const parameters
}

fn foo<const X: u8, T>(_: &T) {}

fn main() {}


