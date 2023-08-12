tests/ui/panics/panic-main.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:moop
// ignore-emscripten no processes

fn main() {
    panic!("moop");
}


