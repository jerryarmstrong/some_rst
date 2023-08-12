tests/ui/fully-qualified-type/fully-qualified-type-name2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we use fully-qualified type names in error messages.

mod x {
    pub enum Foo { }
}

mod y {
    pub enum Foo { }
}

fn bar(x: x::Foo) -> y::Foo {
    return x;
    //~^ ERROR mismatched types
    //~| expected enum `y::Foo`, found enum `x::Foo`
}

fn main() {
}


