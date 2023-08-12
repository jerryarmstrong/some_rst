tests/rustdoc/extern-html-root-url-precedence.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Z unstable-options --extern-html-root-url core=https://example.com/core/0.1.0 --extern-html-root-takes-precedence

// @has extern_html_root_url_precedence/index.html
// --extern-html-root should take precedence if `--takes-precedence` is passed
// @has - '//a/@href' 'https://example.com/core/0.1.0/core/iter/index.html'
#[doc(no_inline)]
pub use std::iter;


