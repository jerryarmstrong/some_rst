tests/ui/associated-item/associated-item-two-bounds.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test is a regression test for #34792

// check-pass

pub struct A;
pub struct B;

pub trait Foo {
    type T: PartialEq<A> + PartialEq<B>;
}

pub fn generic<F: Foo>(t: F::T, a: A, b: B) -> bool {
    t == a && t == b
}

pub fn main() {}


