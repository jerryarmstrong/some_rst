tests/rustdoc/mut-params.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Rustdoc shouldn't display `mut` in function arguments, which are
// implementation details. Regression test for #81289.

#![crate_name = "foo"]

pub struct Foo;

// @count foo/struct.Foo.html '//*[@class="impl-items"]//*[@class="method has-srclink"]' 2
// @!has - '//*[@class="impl-items"]//*[@class="method"]' 'mut'
impl Foo {
    pub fn foo(mut self) {}

    pub fn bar(mut bar: ()) {}
}

// @count foo/fn.baz.html '//div[@class="item-decl"]/pre[@class="rust"]' 1
// @!has - '//div[@class="item-decl"]/pre[@class="rust"]' 'mut'
pub fn baz(mut foo: Foo) {}


