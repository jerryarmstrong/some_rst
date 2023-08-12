tests/ui/coherence/coherence-overlap-upstream-inherent.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we consider `i16: Remote` to be ambiguous, even
// though the upstream crate doesn't implement it for now.

// aux-build:coherence_lib.rs


extern crate coherence_lib;

use coherence_lib::Remote;

struct A<X>(X);
impl<T> A<T> where T: Remote { fn dummy(&self) { } }
//~^ ERROR E0592
impl A<i16> { fn dummy(&self) { } }

fn main() {}


