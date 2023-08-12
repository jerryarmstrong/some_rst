tests/ui/impl-trait/in-trait/trait-more-generics-than-impl.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(return_position_impl_trait_in_trait)]
#![allow(incomplete_features)]

struct S;

trait Foo {
    fn bar<T>() -> impl Sized;
}

impl Foo for S {
    fn bar() -> impl Sized {}
    //~^ ERROR method `bar` has 0 type parameters but its trait declaration has 1 type parameter
}

fn main() {
    S::bar();
}


