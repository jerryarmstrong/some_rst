tests/ui/threads-sendsync/task-life-0.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// ignore-emscripten no threads support
// pretty-expanded FIXME #23616

use std::thread;

pub fn main() {
    thread::spawn(move|| child("Hello".to_string()) ).join();
}

fn child(_s: String) {

}


