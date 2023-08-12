tests/ui/impl-trait/in-trait/reveal.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

trait Foo {
    fn f() -> Box<impl Sized>;
}

impl Foo for () {
    fn f() -> Box<String> {
        Box::new(String::new())
    }
}

fn main() {
    let x: Box<String> = <() as Foo>::f();
}


