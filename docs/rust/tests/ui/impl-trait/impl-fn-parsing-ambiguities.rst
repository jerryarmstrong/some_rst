tests/ui/impl-trait/impl-fn-parsing-ambiguities.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(impl_trait_in_fn_trait_return)]
use std::fmt::Debug;

fn a() -> impl Fn(&u8) -> impl Debug + '_ {
    //~^ ERROR ambiguous `+` in a type
    //~| ERROR higher kinded lifetime bounds on nested opaque types are not supported yet
    |x| x
}

fn b() -> impl Fn() -> impl Debug + Send {
    //~^ ERROR ambiguous `+` in a type
    || ()
}

fn main() {}


