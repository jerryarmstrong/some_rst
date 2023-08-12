src/tools/rustfmt/tests/target/wrap_comments_should_not_imply_format_doc_comments.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: true

/// Foo
///
/// # Example
/// ```
/// # #![cfg_attr(not(dox), feature(cfg_target_feature, target_feature, stdsimd))]
/// # #![cfg_attr(not(dox), no_std)]
/// fn foo() {  }
/// ```
fn foo() {}

/// A long commment for wrapping
/// This is a long long long long long long long long long long long long long
/// long long long long long long long sentence.
fn bar() {}


