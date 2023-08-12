tests/ui/marker_trait_attr/overlapping-impl-1-modulo-regions.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(marker_trait_attr)]

#[marker]
pub trait F {}
impl<T> F for T where T: Copy {}
impl<T> F for T where T: 'static {}

fn main() {}


