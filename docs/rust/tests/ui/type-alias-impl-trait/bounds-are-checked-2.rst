tests/ui/type-alias-impl-trait/bounds-are-checked-2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we check that impl trait types implement the traits that they
// claim to.

#![feature(type_alias_impl_trait)]

type X<T> = impl Clone;

fn f<T: Clone>(t: T) -> X<T> {
    t
    //~^ ERROR the trait bound `T: Clone` is not satisfied
}

fn g<T>(o: Option<X<T>>) -> Option<X<T>> {
    o.clone()
}

fn main() {
    g(None::<X<&mut ()>>);
}


