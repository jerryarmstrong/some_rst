tests/ui/panics/doublepanic.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unreachable_code)]

// run-fail
// error-pattern:One
// ignore-emscripten no processes

fn main() {
    panic!("One");
    panic!("Two");
}


