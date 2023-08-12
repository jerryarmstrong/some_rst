tests/rustdoc/no-run-still-checks-lints.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test
// should-fail

#![doc(test(attr(deny(warnings))))]

/// ```no_run
/// let a = 3;
/// ```
pub fn foo() {}


