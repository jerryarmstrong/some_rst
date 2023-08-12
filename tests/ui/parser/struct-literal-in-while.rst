tests/ui/parser/struct-literal-in-while.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: isize,
}

impl Foo {
    fn hi(&self) -> bool {
        true
    }
}

fn main() {
    while Foo { //~ ERROR struct literals are not allowed here
        x: 3
    }.hi() {
        println!("yo");
    }
}


