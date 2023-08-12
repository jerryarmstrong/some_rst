tests/ui/traits/negative-impls/negative-specializes-negative.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)] //~ WARN the feature `specialization` is incomplete
#![feature(negative_impls)]

// Test a negative impl that "specializes" another negative impl.
//
// run-pass

trait MyTrait {}

impl<T> !MyTrait for T {}
impl !MyTrait for u32 {}

fn main() {}


