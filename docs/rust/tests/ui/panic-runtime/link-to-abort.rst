tests/ui/panic-runtime/link-to-abort.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// compile-flags:-C panic=abort
// no-prefer-dynamic
// ignore-macos

#![feature(panic_abort)]

extern crate panic_abort;

fn main() {}


