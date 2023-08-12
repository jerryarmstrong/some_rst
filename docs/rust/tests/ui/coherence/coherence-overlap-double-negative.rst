tests/ui/coherence/coherence-overlap-double-negative.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(negative_impls)]
#![feature(with_negative_coherence)]

trait A {}
trait B: A {}

impl !A for u32 {}
impl !B for u32 {}

fn main() {}


