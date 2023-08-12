tests/rustdoc/external-macro-src.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:external-macro-src.rs

#![crate_name = "foo"]

#[macro_use]
extern crate external_macro_src;

// @has foo/index.html '//a[@href="../src/foo/external-macro-src.rs.html#3-12"]' 'source'

// @has foo/struct.Foo.html
// @has - '//a[@href="../src/foo/external-macro-src.rs.html#12"]' 'source'
make_foo!();


