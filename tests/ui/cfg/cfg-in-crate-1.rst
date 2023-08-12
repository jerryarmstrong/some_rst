tests/ui/cfg/cfg-in-crate-1.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --cfg bar -D warnings
#![cfg(bar)]

fn main() {}


