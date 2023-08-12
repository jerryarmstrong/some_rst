tests/ui/traits/reservation-impl/coherence-conflict.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that reservation impls are accounted for in negative reasoning.

#![feature(rustc_attrs)]

trait MyTrait {}
#[rustc_reservation_impl="this impl is reserved"]
impl MyTrait for () {}

trait OtherTrait {}
impl OtherTrait for () {}
impl<T: MyTrait> OtherTrait for T {}
//~^ ERROR conflicting implementations

fn main() {}


