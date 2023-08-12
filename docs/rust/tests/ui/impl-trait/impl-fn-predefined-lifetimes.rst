tests/ui/impl-trait/impl-fn-predefined-lifetimes.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(impl_trait_in_fn_trait_return)]
use std::fmt::Debug;

fn a<'a>() -> impl Fn(&'a u8) -> (impl Debug + '_) {
    //~^ ERROR cannot resolve opaque type

    |x| x
    //~^ ERROR concrete type differs from previous defining opaque type use
}

fn _b<'a>() -> impl Fn(&'a u8) -> (impl Debug + 'a) {
    a()
}

fn main() {}


