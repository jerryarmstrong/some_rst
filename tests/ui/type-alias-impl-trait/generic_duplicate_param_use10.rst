tests/ui/type-alias-impl-trait/generic_duplicate_param_use10.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(type_alias_impl_trait)]

use std::fmt::Debug;

fn main() {}

type Two<T: Debug, U> = impl Debug;

fn two<T: Debug, U: Debug>(t: T, _: U) -> Two<T, U> {
    (t, 4u32)
}


