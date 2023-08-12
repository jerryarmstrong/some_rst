tests/ui/pattern/usefulness/irrefutable-let-patterns.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(irrefutable_let_patterns)]

fn main() {
    if let _ = 5 {}

    while let _ = 5 {
        break;
    }
}


