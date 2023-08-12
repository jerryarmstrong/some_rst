tests/ui/coherence/coherence-overlap-negate-use-feature-gate.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(with_negative_coherence)]

use std::ops::DerefMut;

trait Foo {}
impl<T: DerefMut> Foo for T {}
impl<U> Foo for &U {}

fn main() {}


