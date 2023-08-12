tests/rustdoc/intra-doc/enum-struct-field.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub enum Foo {
    X {
        y: u8,
    }
}

/// Hello
///
/// I want [Foo::X::y].
pub fn foo() {}

// @has foo/fn.foo.html '//a/@href' 'enum.Foo.html#variant.X.field.y'


