tests/ui/const-generics/generic_const_exprs/impl-bounds.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

use std::mem::size_of;

struct Foo<T, const N: usize>(T);

impl<T> Foo<T, { size_of::<T>() }> {
    fn test() {
        let _: [u8; std::mem::size_of::<T>()];
    }
}

trait Bar<const N: usize> {
    fn test_me();
}

impl<T> Bar<{ size_of::<T>() }> for Foo<T, 3> {
    fn test_me() {
        let _: [u8; std::mem::size_of::<T>()];
    }
}

fn main() {}


