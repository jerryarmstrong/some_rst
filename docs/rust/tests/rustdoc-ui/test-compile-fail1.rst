tests/rustdoc-ui/test-compile-fail1.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test

/// ```
/// assert!(true)
/// ```
pub fn f() {}

pub fn f() {}


