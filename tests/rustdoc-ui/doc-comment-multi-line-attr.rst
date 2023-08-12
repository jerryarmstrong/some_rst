tests/rustdoc-ui/doc-comment-multi-line-attr.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #97440: Multiline inner attribute triggers ICE during doctest
// compile-flags:--test
// normalize-stdout-test: "tests/rustdoc-ui" -> "$$DIR"
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"
// check-pass

//! ```rust
//! #![deny(
//! unused_parens,
//! )]
//! ```


