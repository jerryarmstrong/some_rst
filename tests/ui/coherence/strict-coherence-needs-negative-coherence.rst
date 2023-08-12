tests/ui/coherence/strict-coherence-needs-negative-coherence.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_strict_coherence]
trait Foo {}
//~^ ERROR to use `strict_coherence` on this trait, the `with_negative_coherence` feature must be enabled

fn main() {}


