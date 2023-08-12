tests/ui/autoref-autoderef/auto-ref.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct Foo {
    x: isize,
}

trait Stuff {
    fn printme(&self);
}

impl Stuff for Foo {
    fn printme(&self) {
        println!("{}", self.x);
    }
}

pub fn main() {
    let x = Foo { x: 3 };
    x.printme();
}


