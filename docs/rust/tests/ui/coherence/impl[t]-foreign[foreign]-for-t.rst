tests/ui/coherence/impl[t]-foreign[foreign]-for-t.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--crate-name=test
// aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::*;
use std::rc::Rc;

struct Local;

impl<T> Remote1<u32> for T {
    //~^ ERROR type parameter `T` must be used as the type parameter for some local type
}

fn main() {}


