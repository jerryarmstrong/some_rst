tests/ui/rfc-2632-const-trait-impl/const-impl-requires-const-trait.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

pub trait A {}
//~^ HELP: mark `A` as const

impl const A for () {}
//~^ ERROR: const `impl` for trait `A` which is not marked with `#[const_trait]`

fn main() {}


