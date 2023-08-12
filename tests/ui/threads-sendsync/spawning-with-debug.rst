tests/ui/threads-sendsync/spawning-with-debug.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
#![allow(unused_mut)]
// ignore-windows
// exec-env:RUST_LOG=debug
// ignore-emscripten no threads support

// regression test for issue #10405, make sure we don't call println! too soon.

use std::thread::Builder;

pub fn main() {
    let mut t = Builder::new();
    t.spawn(move || ());
}


