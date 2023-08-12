tests/ui/try-block/try-block-in-match.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --edition 2018

#![feature(try_blocks)]

fn main() {
    match try { } {
        Err(()) => (),
        Ok(()) => (),
    }
}


