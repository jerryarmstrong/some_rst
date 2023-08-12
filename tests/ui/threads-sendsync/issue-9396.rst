tests/ui/threads-sendsync/issue-9396.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
#![allow(deprecated)]
// ignore-emscripten no threads support

use std::sync::mpsc::{TryRecvError, channel};
use std::thread;

pub fn main() {
    let (tx, rx) = channel();
    let t = thread::spawn(move||{
        thread::sleep_ms(10);
        tx.send(()).unwrap();
    });
    loop {
        match rx.try_recv() {
            Ok(()) => break,
            Err(TryRecvError::Empty) => {}
            Err(TryRecvError::Disconnected) => unreachable!()
        }
    }
    t.join();
}


