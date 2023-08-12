tests/ui/coherence/coherence-iterator-vec.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// aux-build:coherence_lib.rs

// pretty-expanded FIXME #23616

extern crate coherence_lib as lib;
use lib::Remote1;

struct Foo<T>(T);

impl<T> Remote1<T> for Foo<T> { }

fn main() { }


