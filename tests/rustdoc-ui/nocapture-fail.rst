tests/rustdoc-ui/nocapture-fail.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:--test -Zunstable-options --nocapture
// normalize-stderr-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"

/// ```compile_fail
/// fn foo() {
///     Input: 123
/// }
/// ```
pub struct Foo;


