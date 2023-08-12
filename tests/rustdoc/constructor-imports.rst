tests/rustdoc/constructor-imports.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub mod a {
    pub struct Foo;
    pub enum Bar {
        Baz,
    }
}

// @count 'foo/index.html' '//*[code="pub use a::Foo;"]' 1
#[doc(no_inline)]
pub use a::Foo;
// @count 'foo/index.html' '//*[code="pub use a::Bar::Baz;"]' 1
#[doc(no_inline)]
pub use a::Bar::Baz;


