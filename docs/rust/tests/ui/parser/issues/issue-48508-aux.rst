tests/ui/parser/issues/issue-48508-aux.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-test Not a test. Used by issue-48508.rs

pub fn other() -> f64 {
    let µ = 1.0;
    µ
}


