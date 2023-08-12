tests/ui/regions/regions-in-structs-anon.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that anonymous lifetimes are not permitted in struct declarations

struct Foo {
    x: &isize //~ ERROR missing lifetime specifier
}

fn main() {}


