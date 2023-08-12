tests/rustdoc-js/struct-like-variant.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "struct_like_variant"]

pub enum Enum {
    Bar {
        /// This is a name.
        name: String
    }
}


