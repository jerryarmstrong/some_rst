tests/run-make-fulldeps/rustdoc-themes/foo.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has test.css
// @has foo/struct.Foo.html
// @has - '//link[@rel="stylesheet"]/@href' '../test.css'
pub struct Foo;


