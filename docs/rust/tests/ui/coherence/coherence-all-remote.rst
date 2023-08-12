tests/ui/coherence/coherence-all-remote.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::Remote1;

impl<T> Remote1<T> for isize { }
//~^ ERROR E0210

fn main() { }


