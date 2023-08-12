tests/ui/threads-sendsync/issue-4446.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten no threads support

use std::sync::mpsc::channel;
use std::thread;

pub fn main() {
    let (tx, rx) = channel();

    tx.send("hello, world").unwrap();

    thread::spawn(move|| {
        println!("{}", rx.recv().unwrap());
    }).join().ok().unwrap();
}


