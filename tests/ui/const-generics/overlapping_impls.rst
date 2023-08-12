tests/ui/const-generics/overlapping_impls.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(incomplete_features)]
#![feature(adt_const_params)]
#![feature(generic_const_exprs)]
use std::marker::PhantomData;

struct Foo<const I: i32, const J: i32> {}

const ONE: i32 = 1;
const TWO: i32 = 2;

impl<const I: i32> Foo<I, ONE> {
    pub fn foo() {}
}

impl<const I: i32> Foo<I, TWO> {
    pub fn foo() {}
}


pub struct Foo2<const P: Protocol, T> {
    _marker: PhantomData<T>,
}

#[derive(PartialEq, Eq)]
pub enum Protocol {
    Variant1,
    Variant2,
}

pub trait Bar {}

impl<T> Bar for Foo2<{ Protocol::Variant1 }, T> {}
impl<T> Bar for Foo2<{ Protocol::Variant2 }, T> {}

fn main() {}


