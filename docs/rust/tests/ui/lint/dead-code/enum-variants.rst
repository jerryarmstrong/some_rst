tests/ui/lint/dead-code/enum-variants.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(dead_code)]

enum Foo {
    A,
    B,
}

pub fn main() {
    match Foo::A {
        Foo::A | Foo::B => Foo::B
    };
}


