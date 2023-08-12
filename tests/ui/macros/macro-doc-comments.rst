tests/ui/macros/macro-doc-comments.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_snake_case)]

macro_rules! doc {
    (
        $(#[$outer:meta])*
        mod $i:ident {
            $(#![$inner:meta])*
        }
    ) =>
    (
        $(#[$outer])*
        pub mod $i {
            $(#![$inner])*
        }
    )
}

doc! {
    /// Outer doc
    mod Foo {
        //! Inner doc
    }
}

fn main() { }


