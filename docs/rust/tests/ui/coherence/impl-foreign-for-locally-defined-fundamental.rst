tests/ui/coherence/impl-foreign-for-locally-defined-fundamental.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(fundamental)]

// compile-flags:--crate-name=test
// aux-build:coherence_lib.rs
// check-pass

extern crate coherence_lib as lib;
use lib::*;

#[fundamental]
struct Local<T>(T);

impl Remote for Local<()> {}

fn main() {}


