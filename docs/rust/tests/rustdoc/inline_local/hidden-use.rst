tests/rustdoc/inline_local/hidden-use.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod private {
    pub struct Foo {}
}

// @has hidden_use/index.html
// @!hasraw - 'private'
// @!hasraw - 'Foo'
// @!has hidden_use/struct.Foo.html
#[doc(hidden)]
pub use private::Foo;


