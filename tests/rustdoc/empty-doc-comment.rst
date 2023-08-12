tests/rustdoc/empty-doc-comment.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that empty doc comments don't panic.

/*!
*/

///
///
pub struct Foo;

#[doc = "
"]
pub mod Mod {
   //!
   //!
}

/**
*/
pub mod Another {
   #![doc = "
"]
}


