tests/ui/coherence/coherence-overlap-negate-not-use-feature-gate.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::DerefMut;

trait Foo {}
impl<T: DerefMut> Foo for T {}
impl<U> Foo for &U {}
//~^ ERROR: conflicting implementations of trait `Foo` for type `&_` [E0119]

fn main() {}


