tests/rustdoc-ui/doc-test-doctest-feature.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:--test
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"

// Make sure `cfg(doctest)` is set when finding doctests but not inside
// the doctests.

/// ```
/// assert!(!cfg!(doctest));
/// ```
#[cfg(doctest)]
pub struct Foo;


