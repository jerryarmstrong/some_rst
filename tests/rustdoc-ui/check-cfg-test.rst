tests/rustdoc-ui/check-cfg-test.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --test --nocapture --check-cfg=values(feature,"test") -Z unstable-options
// normalize-stderr-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"

/// The doctest will produce a warning because feature invalid is unexpected
/// ```
/// #[cfg(feature = "invalid")]
/// assert!(false);
/// ```
pub struct Foo;


