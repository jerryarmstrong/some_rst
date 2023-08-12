tests/rustdoc/fn-pointer-arg-name.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.f.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub fn f(callback: fn(len: usize, foo: u32))'
pub fn f(callback: fn(len: usize, foo: u32)) {}


