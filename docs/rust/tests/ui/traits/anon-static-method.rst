tests/ui/traits/anon-static-method.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Foo {
    x: isize
}

impl Foo {
    pub fn new() -> Foo {
        Foo { x: 3 }
    }
}

pub fn main() {
    let x = Foo::new();
    println!("{}", x.x);
}


