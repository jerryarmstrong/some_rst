tests/ui/coherence/coherence-lone-type-parameter.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::Remote;

impl<T> Remote for T { }
//~^ ERROR E0210


fn main() { }


