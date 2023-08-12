src/tools/rustfmt/tests/source/doc-comment-with-example.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_code_in_doc_comments: true

/// Foo
///
/// # Example
/// ```
/// # #![cfg_attr(not(dox), feature(cfg_target_feature, target_feature, stdsimd))]
/// # #![cfg_attr(not(dox), no_std)]
/// fn foo() {  }
/// ```
///
fn foo() {}


