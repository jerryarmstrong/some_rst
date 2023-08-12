tests/ui/marker_trait_attr/marker-attribute-with-values.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(marker_trait_attr)]

#[marker(always)] //~ ERROR malformed `marker` attribute
trait Marker1 {}

#[marker("never")] //~ ERROR malformed `marker` attribute
trait Marker2 {}

#[marker(key = "value")] //~ ERROR malformed `marker` attribute
trait Marker3 {}

fn main() {}


