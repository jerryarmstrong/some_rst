tests/ui/dyn-star/upcast.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // known-bug: #104800

#![feature(dyn_star, trait_upcasting)]

trait Foo: Bar {
    fn hello(&self);
}

trait Bar {
    fn world(&self);
}

struct W(usize);

impl Foo for W {
    fn hello(&self) {
        println!("hello!");
    }
}

impl Bar for W {
    fn world(&self) {
        println!("world!");
    }
}

fn main() {
    let w: dyn* Foo = W(0);
    w.hello();
    let w: dyn* Bar = w;
    w.world();
}


