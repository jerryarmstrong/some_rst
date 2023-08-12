tests/ui/type-alias-impl-trait/type-alias-impl-trait-fns.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]

// Regression test for issue #61863

pub trait MyTrait {}

#[derive(Debug)]
pub struct MyStruct {
    v: u64,
}

impl MyTrait for MyStruct {}

pub fn bla() -> TE {
    return MyStruct { v: 1 };
}

pub fn bla2() -> TE {
    bla()
}

type TE = impl MyTrait;

fn main() {}


