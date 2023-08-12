tests/ui/macros/assert-eq-macro-panic.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:assertion failed: `(left == right)`
// error-pattern: left: `14`
// error-pattern:right: `15`
// ignore-emscripten no processes

fn main() {
    assert_eq!(14, 15);
}


