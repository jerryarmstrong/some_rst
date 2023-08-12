tests/ui/structs/struct-fields-shorthand.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: i32,
    y: i32
}

fn main() {
    let (x, y, z) = (0, 1, 2);
    let foo = Foo {
        x, y, z //~ ERROR struct `Foo` has no field named `z`
    };
}


