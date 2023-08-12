tests/rustdoc-ui/doc-test-rustdoc-feature.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:--test
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"

#![feature(doc_cfg)]

// Make sure `cfg(doc)` is set when finding doctests but not inside the doctests.

/// ```
/// #![feature(doc_cfg)]
/// assert!(!cfg!(doc));
/// ```
#[cfg(doc)]
pub struct Foo;


