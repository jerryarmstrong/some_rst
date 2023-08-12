tests/ui/lint/let_underscore/let_underscore_lock.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
use std::sync::{Arc, Mutex};

fn main() {
    let data = Arc::new(Mutex::new(0));
    let _ = data.lock().unwrap(); //~ERROR non-binding let on a synchronization lock
}


