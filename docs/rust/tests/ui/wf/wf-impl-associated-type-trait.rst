tests/ui/wf/wf-impl-associated-type-trait.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we require that associated types in an impl are well-formed.


#![allow(dead_code)]

pub trait MyHash { }

pub struct MySet<T:MyHash> {
    data: Vec<T>
}

pub trait Foo {
    type Bar;
}

impl<T> Foo for T {
    type Bar = MySet<T>;
    //~^ ERROR the trait bound `T: MyHash` is not satisfied
}


fn main() { }


