tests/ui/traits/negative-impls/positive-specializes-negative.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)] //~ WARN the feature `specialization` is incomplete
#![feature(negative_impls)]

trait MyTrait {}

impl<T> !MyTrait for T {}
impl MyTrait for u32 {} //~ ERROR E0751

fn main() {}


