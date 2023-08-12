tests/ui/tuple/wrong_argument_ice-2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test(t: (i32, i32)) {}

struct Foo;

impl Foo {
    fn qux(&self) -> i32 {
        0
    }
}

fn bar() {
    let x = Foo;
    test(x.qux(), x.qux());
    //~^ ERROR function takes 1 argument but 2 arguments were supplied
}

fn main() {}


