tests/ui/lifetimes/conflicting-bounds.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //~ type annotations needed: cannot satisfy `Self: Gen<'source>`

pub trait Gen<'source> {
    type Output;

    fn gen<T>(&self) -> T
    where
        Self: for<'s> Gen<'s, Output = T>;
}

fn main() {}


