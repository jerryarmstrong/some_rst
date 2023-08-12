tests/ui/pattern/usefulness/deny-irrefutable-let-patterns.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

#![deny(irrefutable_let_patterns)]

fn main() {
    if let _ = 5 {} //~ ERROR irrefutable `if let` pattern

    while let _ = 5 { //~ ERROR irrefutable `while let` pattern
        break;
    }

    match 5 {
        _ if let _ = 2 => {} //~ ERROR irrefutable `if let` guard pattern
        _ => {}
    }
}


