tests/rustdoc/range-arg-pattern.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.f.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub fn f(_: u8)'
pub fn f(0u8..=255: u8) {}


