tests/ui/dyn-star/box.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -C opt-level=0

#![feature(dyn_star)]
#![allow(incomplete_features)]

use std::fmt::Display;

fn make_dyn_star() -> dyn* Display {
    Box::new(42) as dyn* Display
}

fn main() {
    let x = make_dyn_star();

    println!("{x}");
}


