tests/rustdoc/auxiliary/primitive-reexport.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit metadata --crate-type lib --edition 2018

#![crate_name = "foo"]

pub mod bar {
    pub use bool;
    pub use char as my_char;
}


