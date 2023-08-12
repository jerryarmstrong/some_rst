tests/ui/threads-sendsync/spawn.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten no threads support

use std::thread;

pub fn main() {
    thread::spawn(move|| child(10)).join().ok().unwrap();
}

fn child(i: isize) { println!("{}", i); assert_eq!(i, 10); }


