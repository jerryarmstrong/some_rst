tests/ui/traits/negative-impls/negative-specializes-positive.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)] //~ WARN the feature `specialization` is incomplete
#![feature(negative_impls)]

// Negative impl for u32 cannot "specialize" the base impl.
trait MyTrait {}
impl<T> MyTrait for T {}
impl !MyTrait for u32 {} //~ ERROR E0751

// The second impl specializes the first, no error.
trait MyTrait2 {}
impl<T> MyTrait2 for T {}
impl MyTrait2 for u32 {}

fn main() {}


