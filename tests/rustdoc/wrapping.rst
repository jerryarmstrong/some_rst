tests/rustdoc/wrapping.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

// @has 'wrapping/fn.foo.html' '//div[@class="item-decl"]/pre[@class="rust"]' 'pub fn foo() -> impl Debug'
// @count - '//div[@class="item-decl"]/pre[@class="rust"]/br' 0
pub fn foo() -> impl Debug {}


