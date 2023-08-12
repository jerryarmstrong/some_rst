tests/ui/consts/const-nullary-enum.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum Foo {
    Bar,
    Baz,
    Boo,
}

static X: Foo = Foo::Bar;

pub fn main() {
    match X {
        Foo::Bar => {}
        Foo::Baz | Foo::Boo => panic!()
    }
    match Y {
        Foo::Baz => {}
        Foo::Bar | Foo::Boo => panic!()
    }
}

static Y: Foo = Foo::Baz;


