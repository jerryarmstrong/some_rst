tests/ui/threads-sendsync/trivial-message.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_must_use)]
/*
  This is about the simplest program that can successfully send a
  message.
 */

use std::sync::mpsc::channel;

pub fn main() {
    let (tx, rx) = channel();
    tx.send(42);
    let r = rx.recv();
    println!("{:?}", r);
}


