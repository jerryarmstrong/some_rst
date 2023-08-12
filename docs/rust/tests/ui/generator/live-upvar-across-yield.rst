tests/ui/generator/live-upvar-across-yield.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(generators, generator_trait)]

use std::ops::Generator;
use std::pin::Pin;

fn main() {
    let b = |_| 3;
    let mut a = || {
        b(yield);
    };
    Pin::new(&mut a).resume(());
}


