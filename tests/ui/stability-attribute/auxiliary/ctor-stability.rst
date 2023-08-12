tests/ui/stability-attribute/auxiliary/ctor-stability.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(staged_api)]
#![stable(feature = "none", since = "1.0")]

#[stable(feature = "none", since = "1.0")]
pub enum Foo {
    A,
}


