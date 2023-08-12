tests/ui/rfc-2632-const-trait-impl/generic-bound.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(const_trait_impl)]

use std::marker::PhantomData;

struct S<T>(PhantomData<T>);

impl<T> Copy for S<T> {}
impl<T> Clone for S<T> {
    fn clone(&self) -> Self {
        S(PhantomData)
    }
}

impl<T> const std::ops::Add for S<T> {
    type Output = Self;

    fn add(self, _: Self) -> Self {
        S(std::marker::PhantomData)
    }
}

const fn twice<T: std::ops::Add>(arg: S<T>) -> S<T> {
    arg + arg
}

fn main() {
    let _ = twice(S(PhantomData::<i32>));
}


