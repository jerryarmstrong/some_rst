tests/ui/threads-sendsync/yield1.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_must_use)]
#![allow(unused_mut)]
// ignore-emscripten no threads support

use std::thread;

pub fn main() {
    let mut result = thread::spawn(child);
    println!("1");
    thread::yield_now();
    result.join();
}

fn child() { println!("2"); }


