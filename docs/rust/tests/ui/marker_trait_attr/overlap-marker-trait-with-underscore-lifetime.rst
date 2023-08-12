tests/ui/marker_trait_attr/overlap-marker-trait-with-underscore-lifetime.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(marker_trait_attr)]

#[marker]
trait Marker {}

impl Marker for &'_ () {} //~ ERROR type annotations needed
impl Marker for &'_ () {} //~ ERROR type annotations needed

fn main() {}


