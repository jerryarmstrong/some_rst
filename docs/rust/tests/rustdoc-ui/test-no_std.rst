tests/rustdoc-ui/test-no_std.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"
// check-pass

#![no_std]

extern crate alloc;

/// ```
/// assert!(true)
/// ```
pub fn f() {}


