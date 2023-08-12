tests/ui/coherence/coherence-pair-covered-uncovered-1.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the same coverage rules apply even if the local type appears in the
// list of type parameters, not the self type.

// aux-build:coherence_lib.rs


extern crate coherence_lib as lib;
use lib::{Remote1, Pair};

pub struct Local<T>(T);

impl<T, U> Remote1<Pair<T, Local<U>>> for i32 { }
//~^ ERROR E0117

fn main() { }


