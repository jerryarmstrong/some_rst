tests/ui/save-analysis/emit-notifications.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// compile-flags: -Zsave-analysis --json artifacts
// compile-flags: --crate-type rlib --error-format=json
// ignore-pass
// ^-- needed because otherwise, the .stderr file changes with --pass check

pub fn foo() {}


