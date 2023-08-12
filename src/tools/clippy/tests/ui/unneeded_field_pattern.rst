src/tools/clippy/tests/ui/unneeded_field_pattern.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::unneeded_field_pattern)]
#[allow(dead_code, unused)]

struct Foo {
    a: i32,
    b: i32,
    c: i32,
}

fn main() {
    let f = Foo { a: 0, b: 0, c: 0 };

    match f {
        Foo { a: _, b: 0, .. } => {},

        Foo { a: _, b: _, c: _ } => {},
    }
    match f {
        Foo { b: 0, .. } => {}, // should be OK
        Foo { .. } => {},       // and the Force might be with this one
    }
}


