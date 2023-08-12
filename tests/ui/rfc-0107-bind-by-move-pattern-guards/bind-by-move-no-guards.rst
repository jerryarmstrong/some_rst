tests/ui/rfc-0107-bind-by-move-pattern-guards/bind-by-move-no-guards.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Adaptation of existing ui test (from way back in
// rust-lang/rust#2329), that starts passing with this feature in
// place.

// run-pass

use std::sync::mpsc::channel;

fn main() {
    let (tx, rx) = channel();
    let x = Some(rx);
    tx.send(false).unwrap();
    tx.send(false).unwrap();
    match x {
        Some(z) if z.recv().unwrap() => { panic!() },
        Some(z) => { assert!(!z.recv().unwrap()); },
        None => panic!()
    }
}


