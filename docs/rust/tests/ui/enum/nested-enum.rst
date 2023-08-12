tests/ui/enum/nested-enum.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    enum Bar { Baz }, //~ ERROR `enum` definition cannot be nested inside `enum`
    struct Quux { field: u8 }, //~ ERROR `struct` definition cannot be nested inside `enum`
    union Wibble { field: u8 }, //~ ERROR `union` definition cannot be nested inside `enum`
    Bat,
}

fn main() { }


