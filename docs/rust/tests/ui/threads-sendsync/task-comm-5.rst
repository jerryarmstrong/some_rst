tests/ui/threads-sendsync/task-comm-5.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::sync::mpsc::channel;

pub fn main() { test00(); }

fn test00() {
    let _r: isize = 0;
    let mut sum: isize = 0;
    let (tx, rx) = channel();
    let number_of_messages: isize = 1000;
    let mut i: isize = 0;
    while i < number_of_messages { tx.send(i + 0).unwrap(); i += 1; }
    i = 0;
    while i < number_of_messages { sum += rx.recv().unwrap(); i += 1; }
    assert_eq!(sum, number_of_messages * (number_of_messages - 1) / 2);
}


