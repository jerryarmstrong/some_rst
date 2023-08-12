tests/rustdoc/search-index-summaries.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @hasraw 'search-index.js' 'Foo short link.'
// @!hasraw - 'www.example.com'
// @!hasraw - 'More Foo.'

/// Foo short [link](https://www.example.com/).
///
/// More Foo.
pub struct Foo;


