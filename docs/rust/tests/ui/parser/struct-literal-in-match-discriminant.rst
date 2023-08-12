tests/ui/parser/struct-literal-in-match-discriminant.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: isize,
}

fn main() {
    match Foo { //~ ERROR struct literals are not allowed here
        x: 3
    } {
        Foo {
            x: x
        } => {}
    }
}


