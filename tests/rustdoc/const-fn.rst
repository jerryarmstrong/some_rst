tests/rustdoc/const-fn.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.bar.html
// @has - '//div[@class="item-decl"]/pre[@class="rust"]' 'pub const fn bar() -> '
/// foo
pub const fn bar() -> usize {
    2
}

// @has foo/struct.Foo.html
// @has - '//*[@class="method has-srclink"]' 'const fn new()'
pub struct Foo(usize);

impl Foo {
    pub const fn new() -> Foo { Foo(0) }
}


