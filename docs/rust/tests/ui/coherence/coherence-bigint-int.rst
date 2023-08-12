tests/ui/coherence/coherence-bigint-int.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:coherence_lib.rs

// pretty-expanded FIXME #23616

extern crate coherence_lib as lib;
use lib::Remote1;

pub struct BigInt;

impl Remote1<BigInt> for isize { }

fn main() { }


