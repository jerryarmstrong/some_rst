tests/ui/structs-enums/variant-structs-trivial.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

enum Foo {
    Bar { x: isize },
    Baz { y: isize }
}

pub fn main() { }


