tests/rustdoc/where-sized.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.foo.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub fn foo<X, Y: ?Sized>(_: &X)'
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'where X: ?Sized,'
pub fn foo<X, Y: ?Sized>(_: &X) where X: ?Sized {}


