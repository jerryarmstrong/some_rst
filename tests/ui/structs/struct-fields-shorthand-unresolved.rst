tests/ui/structs/struct-fields-shorthand-unresolved.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: i32,
    y: i32
}

fn main() {
    let x = 0;
    let foo = Foo {
        x,
        y //~ ERROR cannot find value `y` in this scope
    };
}


