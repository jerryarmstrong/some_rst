tests/ui/issues/issue-2761.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:custom message
// ignore-emscripten no processes

fn main() {
    assert!(false, "custom message");
}


