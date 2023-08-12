tests/ui/marker_trait_attr/overlap-marker-trait-with-static-lifetime.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(marker_trait_attr)]

#[marker]
trait Marker {}

impl Marker for &'static () {}
impl Marker for &'static () {}

fn main() {}


