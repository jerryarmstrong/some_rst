tests/rustdoc/index-page.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:all-item-types.rs
// build-aux-docs
// compile-flags: -Z unstable-options --enable-index-page

#![crate_name = "foo"]

// @has foo/../index.html
// @has - '//h1' 'List of all crates'
// @has - '//ul[@class="all-items"]//a[@href="foo/index.html"]' 'foo'
// @has - '//ul[@class="all-items"]//a[@href="all_item_types/index.html"]' 'all_item_types'
pub struct Foo;


