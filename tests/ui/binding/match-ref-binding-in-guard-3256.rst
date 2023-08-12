tests/ui/binding/match-ref-binding-in-guard-3256.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::sync::Mutex;

pub fn main() {
    let x = Some(Mutex::new(true));
    match x {
        Some(ref z) if *z.lock().unwrap() => {
            assert!(*z.lock().unwrap());
        },
        _ => panic!()
    }
}


