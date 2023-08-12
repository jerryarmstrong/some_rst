tests/ui/threads-sendsync/task-comm-17.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// ignore-emscripten no threads support
// pretty-expanded FIXME #23616

// Issue #922

// This test is specifically about spawning temporary closures.

use std::thread;

fn f() {
}

pub fn main() {
    thread::spawn(move|| f() ).join();
}


