tests/rustdoc/hidden-impls.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

mod hidden {
    #[derive(Clone)]
    pub struct Foo;
}

#[doc(hidden)]
pub mod __hidden {
    pub use hidden::Foo;
}

// @has foo/trait.Clone.html
// @!hasraw - 'Foo'
// @has implementors/core/clone/trait.Clone.js
// @!hasraw - 'Foo'
pub use std::clone::Clone;


