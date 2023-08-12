tests/ui/anon-params/anon-params-edition-hygiene.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
// aux-build:anon-params-edition-hygiene.rs

// This warning is still surfaced
#![allow(anonymous_parameters)]

#[macro_use]
extern crate anon_params_edition_hygiene;

generate_trait_2015!(u8);

fn main() {}


