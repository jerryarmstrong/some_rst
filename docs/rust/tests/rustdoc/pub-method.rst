tests/rustdoc/pub-method.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --document-private-items

#![crate_name = "foo"]

// @has foo/fn.bar.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub fn bar() -> '
/// foo
pub fn bar() -> usize {
    2
}

// @has foo/struct.Foo.html
// @has - '//*[@class="method has-srclink"]' 'pub fn new()'
// @has - '//*[@class="method has-srclink"]' 'fn not_pub()'
pub struct Foo(usize);

impl Foo {
    pub fn new() -> Foo { Foo(0) }
    fn not_pub() {}
}


