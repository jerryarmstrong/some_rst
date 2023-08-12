tests/ui/regions/regions-in-enums-anon.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that anonymous lifetimes are not permitted in enum declarations

enum Foo {
    Bar(&isize) //~ ERROR missing lifetime specifier
}

fn main() {}


