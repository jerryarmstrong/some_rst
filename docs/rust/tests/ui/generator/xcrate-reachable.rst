tests/ui/generator/xcrate-reachable.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// aux-build:xcrate-reachable.rs

#![feature(generator_trait)]

extern crate xcrate_reachable as foo;

use std::ops::Generator;
use std::pin::Pin;

fn main() {
    Pin::new(&mut foo::foo()).resume(());
}


