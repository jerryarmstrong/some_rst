tests/ui/enum/enum-variant-type-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that enum variants are not actually types.

enum Foo {
    Bar
}

fn foo(x: Foo::Bar) {} //~ ERROR expected type, found variant `Foo::Bar`

fn main() {}


