tests/ui/macros/assert-ne-macro-panic.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:assertion failed: `(left != right)`
// error-pattern: left: `14`
// error-pattern:right: `14`
// ignore-emscripten no processes

fn main() {
    assert_ne!(14, 14);
}


