tests/ui/reachable/unreachable-code-ret.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: unreachable statement

#![deny(unreachable_code)]

fn main() {
    return;
    println!("Paul is dead");
}


