tests/rustdoc/const.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

pub struct Foo;

impl Foo {
    // @has const/struct.Foo.html '//*[@id="method.new"]//h4[@class="code-header"]' 'const unsafe fn new'
    pub const unsafe fn new() -> Foo {
        Foo
    }
}


