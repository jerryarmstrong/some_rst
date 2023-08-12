tests/rustdoc/auxiliary/primitive-doc.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type lib --edition 2018

#![feature(no_core)]
#![no_core]

#[doc(primitive = "usize")]
/// This is the built-in type `usize`.
mod usize {
}


