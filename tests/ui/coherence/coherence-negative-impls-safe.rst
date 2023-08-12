tests/ui/coherence/coherence-negative-impls-safe.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

use std::marker::Send;

struct TestType;

unsafe impl !Send for TestType {}
//~^ ERROR E0198

fn main() {}


