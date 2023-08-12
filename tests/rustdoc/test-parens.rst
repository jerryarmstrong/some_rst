tests/rustdoc/test-parens.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.foo.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' "_: &(dyn ToString + 'static)"
pub fn foo(_: &(ToString + 'static)) {}


