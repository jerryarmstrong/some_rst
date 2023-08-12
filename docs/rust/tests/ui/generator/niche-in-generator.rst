tests/ui/generator/niche-in-generator.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that niche finding works with captured generator upvars.

// run-pass

#![feature(generators)]

use std::mem::size_of_val;

fn take<T>(_: T) {}

fn main() {
    let x = false;
    let gen1 = || {
        yield;
        take(x);
    };

    assert_eq!(size_of_val(&gen1), size_of_val(&Some(gen1)));
}


