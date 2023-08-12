tests/ui/coherence/coherence-overlap-with-regions.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(negative_impls)]
#![feature(rustc_attrs)]
#![feature(with_negative_coherence)]

#[rustc_strict_coherence]
trait Foo {}
impl<T> !Foo for &T where T: 'static {}

#[rustc_strict_coherence]
trait Bar {}
impl<T: Foo> Bar for T {}
impl<T> Bar for &T where T: 'static {}

fn main() {}


