tests/ui/coherence/coherence-overlap-negative-trait.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:error_lib.rs
//
// Check that if we promise to not impl what would overlap it doesn't actually overlap

#![feature(with_negative_coherence)]

extern crate error_lib as lib;
use lib::Error;

trait From<T> {}

impl From<&str> for Box<dyn Error> {}
impl<E> From<E> for Box<dyn Error> where E: Error {}

fn main() {}


