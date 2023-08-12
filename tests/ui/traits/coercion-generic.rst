tests/ui/traits/coercion-generic.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
trait Trait<T> {
    fn f(&self, x: T);
}

#[derive(Copy, Clone)]
struct Struct {
    x: isize,
    y: isize,
}

impl Trait<&'static str> for Struct {
    fn f(&self, x: &'static str) {
        println!("Hi, {}!", x);
    }
}

pub fn main() {
    let a = Struct { x: 1, y: 2 };
    let b: Box<dyn Trait<&'static str>> = Box::new(a);
    b.f("Mary");
    let c: &dyn Trait<&'static str> = &a;
    c.f("Joe");
}


