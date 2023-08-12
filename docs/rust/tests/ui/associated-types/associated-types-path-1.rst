tests/ui/associated-types/associated-types-path-1.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we have one and only one associated type per ref.

pub trait Foo {
    type A;
}
pub trait Bar {
    type A;
}

pub fn f1<T>(a: T, x: T::A) {} //~ERROR associated type `A` not found
pub fn f2<T: Foo + Bar>(a: T, x: T::A) {} //~ERROR ambiguous associated type `A`

pub fn main() {}


