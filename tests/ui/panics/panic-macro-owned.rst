tests/ui/panics/panic-macro-owned.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:panicked at 'test-fail-owned'
// ignore-emscripten no processes

fn main() {
    panic!("test-fail-owned");
}


