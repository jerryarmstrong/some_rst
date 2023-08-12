tests/rustdoc-ui/doctest-multiline-crate-attribute.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:--test --test-args=--test-threads=1
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"
// check-pass

/// ```
/// #![deprecated(since = "5.2", note = "foo was rarely used. \
///    Users should instead use bar")]
/// ```
pub fn f() {}


