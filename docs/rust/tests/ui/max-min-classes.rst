tests/ui/max-min-classes.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_snake_case)]
trait Product {
    fn product(&self) -> isize;
}

struct Foo {
    x: isize,
    y: isize,
}

impl Foo {
    pub fn sum(&self) -> isize {
        self.x + self.y
    }
}

impl Product for Foo {
    fn product(&self) -> isize {
        self.x * self.y
    }
}

fn Foo(x: isize, y: isize) -> Foo {
    Foo { x: x, y: y }
}

pub fn main() {
    let foo = Foo(3, 20);
    println!("{} {}", foo.sum(), foo.product());
}


