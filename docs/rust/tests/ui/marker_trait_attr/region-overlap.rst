tests/ui/marker_trait_attr/region-overlap.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(marker_trait_attr)]

#[marker]
trait A {}
impl<'a> A for (&'static (), &'a ()) {} //~ ERROR type annotations needed
impl<'a> A for (&'a (), &'static ()) {} //~ ERROR type annotations needed

fn main() {}


