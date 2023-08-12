tests/ui/structs-enums/struct-like-variant-construct.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

enum Foo {
    Bar {
        a: isize,
        b: isize
    },
    Baz {
        c: f64,
        d: f64
    }
}

pub fn main() {
    let _x = Foo::Bar { a: 2, b: 3 };
}


