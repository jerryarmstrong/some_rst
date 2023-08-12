tests/ui/rfc-2397-do-not-recommend/feature-gate-do_not_recommend.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(do_not_recommend)]

pub trait Foo {
}

impl Foo for i32 {
}

pub trait Bar {
}

#[do_not_recommend]
impl<T: Foo> Bar for T {
}

fn stuff<T: Bar>(_: T) {}

fn main() {
    stuff(1u8);
    //~^ the trait bound `u8: Foo` is not satisfied
}


