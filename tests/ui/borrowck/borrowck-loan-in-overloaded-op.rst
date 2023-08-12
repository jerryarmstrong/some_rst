tests/ui/borrowck/borrowck-loan-in-overloaded-op.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_patterns)]


use std::ops::Add;

#[derive(Clone)]
struct Foo(Box<usize>);

impl Add for Foo {
    type Output = Foo;

    fn add(self, f: Foo) -> Foo {
        let Foo(box i) = self;
        let Foo(box j) = f;
        Foo(Box::new(i + j))
    }
}

fn main() {
    let x = Foo(Box::new(3));
    let _y = {x} + x.clone(); // the `{x}` forces a move to occur
    //~^ ERROR borrow of moved value: `x`
}


