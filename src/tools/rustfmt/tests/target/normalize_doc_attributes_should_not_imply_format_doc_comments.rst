src/tools/rustfmt/tests/target/normalize_doc_attributes_should_not_imply_format_doc_comments.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_doc_attributes: true

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

///Bar documents
fn bar() {}


