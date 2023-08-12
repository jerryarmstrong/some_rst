src/tools/rustfmt/tests/source/invalid-rust-code-in-doc-comment.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_code_in_doc_comments: true

/// ```rust
/// if (true) { … }
/// ```
fn a() {
}

/// ```rust
/// if foo() {
///     …
/// }
/// ```
fn a() {
}

/// ```rust
/// k1 == k2 ⇒ hash(k1) == hash(k2)
/// ```
pub   struct   a   ;


