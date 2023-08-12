tests/ui/threads-sendsync/task-comm-11.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// pretty-expanded FIXME #23616
// ignore-emscripten no threads support

use std::sync::mpsc::{channel, Sender};
use std::thread;

fn start(tx: &Sender<Sender<isize>>) {
    let (tx2, _rx) = channel();
    tx.send(tx2).unwrap();
}

pub fn main() {
    let (tx, rx) = channel();
    let child = thread::spawn(move|| {
        start(&tx)
    });
    let _tx = rx.recv().unwrap();
    child.join();
}


