tests/ui/panics/panic.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:1 == 2
// ignore-emscripten no processes

fn main() {
    assert!(1 == 2);
}


