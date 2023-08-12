tests/ui/coherence/coherence-pair-covered-uncovered.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::{Remote, Pair};

struct Local<T>(T);

impl<T,U> Remote for Pair<T,Local<U>> { }
//~^ ERROR E0117

fn main() { }


