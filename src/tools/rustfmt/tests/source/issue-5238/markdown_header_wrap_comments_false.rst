src/tools/rustfmt/tests/source/issue-5238/markdown_header_wrap_comments_false.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: false

/// no markdown header so rustfmt should wrap this comment when `format_code_in_doc_comments = true` and `wrap_comments = true`
fn not_documented_with_markdown_header() {
    // This is just a normal inline comment so rustfmt should wrap this comment when `wrap_comments = true`
}

/// # We're using a markdown header here so rustfmt should refuse to wrap this comment in all circumstances
fn documented_with_markdown_header() {
    // # We're using a markdown header in an inline comment. rustfmt should be able to wrap this comment when `wrap_comments = true`
}


