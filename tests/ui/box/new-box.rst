tests/ui/box/new-box.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(x: Box<isize>) {
    let y: &isize = &*x;
    println!("{}", *x);
    println!("{}", *y);
}

trait Trait {
    fn printme(&self);
}

struct Struct;

impl Trait for Struct {
    fn printme(&self) {
        println!("hello world!");
    }
}

fn g(x: Box<dyn Trait>) {
    x.printme();
    let y: &dyn Trait = &*x;
    y.printme();
}

fn main() {
    f(Box::new(1234));
    g(Box::new(Struct) as Box<dyn Trait>);
}


