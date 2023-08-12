tests/ui/coherence/coherence-overlap-super-negative.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(negative_impls)]
#![feature(rustc_attrs)]
#![feature(with_negative_coherence)]

trait Trait1: Trait2 {}
trait Trait2 {}

struct MyType {}
impl !Trait2 for MyType {}

#[rustc_strict_coherence]
trait Foo {}
impl<T: Trait1> Foo for T {}
impl Foo for MyType {}

fn main() {}


