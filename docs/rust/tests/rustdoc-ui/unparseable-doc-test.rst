tests/rustdoc-ui/unparseable-doc-test.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"
// failure-status: 101
// rustc-env: RUST_BACKTRACE=0

/// ```rust
/// let x = 7;
/// "unterminated
/// ```
pub fn foo() {}


