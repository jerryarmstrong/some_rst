tests/rustdoc/inline_local/please_inline.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod foo {
    pub struct Foo;
}

// @has please_inline/a/index.html
pub mod a {
    // @!hasraw - 'pub use foo::'
    // @has please_inline/a/struct.Foo.html
    #[doc(inline)]
    pub use foo::Foo;
}

// @has please_inline/b/index.html
pub mod b {
    // @hasraw - 'pub use foo::'
    // @!has please_inline/b/struct.Foo.html
    #[feature(inline)]
    pub use foo::Foo;
}


