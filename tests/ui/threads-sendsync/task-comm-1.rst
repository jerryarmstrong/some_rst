tests/ui/threads-sendsync/task-comm-1.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// ignore-emscripten no threads support

use std::thread;

pub fn main() { test00(); }

fn start() { println!("Started / Finished task."); }

fn test00() {
    thread::spawn(move|| start() ).join();
    println!("Completing.");
}


