tests/ui/type/type-parameter-names.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we print out the names of type parameters correctly in
// our error messages.

fn foo<Foo, Bar>(x: Foo) -> Bar {
    x
//~^ ERROR mismatched types
//~| expected type parameter `Bar`, found type parameter `Foo`
//~| expected type parameter `Bar`
//~| found type parameter `Foo`
}

fn main() {}


