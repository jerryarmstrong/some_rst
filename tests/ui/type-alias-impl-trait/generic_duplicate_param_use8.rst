tests/ui/type-alias-impl-trait/generic_duplicate_param_use8.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

use std::fmt::Debug;

fn main() {}

type Two<T, U> = impl Debug;

fn two<T: Debug, U: Debug>(t: T, _: U) -> Two<T, U> {
    (t, 4u32)
    //~^ ERROR `T` doesn't implement `Debug`
}

fn three<T: Debug, U: Debug>(_: T, u: U) -> Two<T, U> {
    (u, 4u32)
    //~^ ERROR `U` doesn't implement `Debug`
}


