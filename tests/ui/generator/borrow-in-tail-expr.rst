tests/ui/generator/borrow-in-tail-expr.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(generators)]

fn main() {
    let _a = || {
        yield;
        let a = String::new();
        a.len()
    };
}


