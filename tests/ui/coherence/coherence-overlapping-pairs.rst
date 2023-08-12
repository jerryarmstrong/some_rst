tests/ui/coherence/coherence-overlapping-pairs.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::Remote;

struct Foo;

impl<T> Remote for lib::Pair<T,Foo> { }
//~^ ERROR E0117

fn main() { }


