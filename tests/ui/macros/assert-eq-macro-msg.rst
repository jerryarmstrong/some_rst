tests/ui/macros/assert-eq-macro-msg.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:panicked at 'assertion failed: `(left == right)`
// error-pattern: left: `2`
// error-pattern:right: `3`: 1 + 1 definitely should be 3'
// ignore-emscripten no processes

fn main() {
    assert_eq!(1 + 1, 3, "1 + 1 definitely should be 3");
}


