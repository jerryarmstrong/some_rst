tests/ui/threads-sendsync/issue-4448.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten no threads support

use std::sync::mpsc::channel;
use std::thread;

pub fn main() {
    let (tx, rx) = channel::<&'static str>();

    let t = thread::spawn(move|| {
        assert_eq!(rx.recv().unwrap(), "hello, world");
    });

    tx.send("hello, world").unwrap();
    t.join().ok().unwrap();
}


