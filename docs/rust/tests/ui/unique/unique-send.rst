tests/ui/unique/unique-send.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::sync::mpsc::channel;

pub fn main() {
    let (tx, rx) = channel::<Box<_>>();
    tx.send(Box::new(100)).unwrap();
    let v = rx.recv().unwrap();
    assert_eq!(v, Box::new(100));
}


