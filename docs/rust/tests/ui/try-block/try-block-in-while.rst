tests/ui/try-block/try-block-in-while.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018

#![feature(try_blocks)]

fn main() {
    while try { false } {}
    //~^ ERROR a `try` block must
}


