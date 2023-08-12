tests/ui/type-alias-impl-trait/generic_duplicate_param_use2.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

use std::fmt::Debug;

fn main() {}

// test that unused generic parameters are ok
type Two<T, U> = impl Debug;

fn two<T: Debug, U>(t: T, _: U) -> Two<T, U> {
    t
    //~^ ERROR `T` doesn't implement `Debug`
}


