tests/ui/cross-crate/auxiliary/cci_capture_clause.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::thread;
use std::sync::mpsc::{Receiver, channel};

pub fn foo<T:'static + Send + Clone>(x: T) -> Receiver<T> {
    let (tx, rx) = channel();
    thread::spawn(move|| {
        tx.send(x.clone());
    });
    rx
}


