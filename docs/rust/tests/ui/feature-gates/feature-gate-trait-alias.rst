tests/ui/feature-gates/feature-gate-trait-alias.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo = Default;
//~^ ERROR trait aliases are experimental

fn main() {}


