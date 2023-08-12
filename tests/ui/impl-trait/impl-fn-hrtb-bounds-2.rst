tests/ui/impl-trait/impl-fn-hrtb-bounds-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(impl_trait_in_fn_trait_return)]
use std::fmt::Debug;

fn a() -> impl Fn(&u8) -> impl Debug {
    |x| x //~ ERROR hidden type for `impl Debug` captures lifetime that does not appear in bounds
}

fn main() {}


