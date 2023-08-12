tests/ui/rfc-2632-const-trait-impl/impl-tilde-const-trait.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

struct S;
trait T {}

impl ~const T for S {}
//~^ ERROR expected a trait, found type

fn main() {}


