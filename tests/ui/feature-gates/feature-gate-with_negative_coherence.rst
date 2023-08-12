tests/ui/feature-gates/feature-gate-with_negative_coherence.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo { }

impl<T: std::ops::DerefMut> Foo for T { }

impl<T> Foo for &T { }
//~^ ERROR conflicting implementations of trait `Foo` for type `&_` [E0119]

fn main() { }


