tests/ui/imports/glob-use-std.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #7580

// run-fail
// error-pattern:panic works
// ignore-emscripten no processes

use std::*;

fn main() {
    panic!("panic works")
}


