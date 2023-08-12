tests/ui/coherence/coherence-projection-ok.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

pub trait Foo<P> {}

pub trait Bar {
    type Output: 'static;
}

impl Foo<i32> for i32 { }

impl<A:Bar> Foo<A::Output> for A { }

impl Bar for i32 {
    type Output = u32;
}

fn main() {}


