tests/ui/borrowck/borrowck-auto-mut-ref-to-immut-var.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that auto-ref can't create mutable aliases to immutable memory.

struct Foo {
    x: isize
}

impl Foo {
    pub fn printme(&mut self) {
        println!("{}", self.x);
    }
}

fn main() {
    let x = Foo { x: 3 };
    x.printme();    //~ ERROR cannot borrow
}


