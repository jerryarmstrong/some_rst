tests/ui/rustdoc/renamed-features-rustdoc_internals.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(doc_keyword)] //~ ERROR
#![feature(doc_primitive)] //~ ERROR
#![crate_type = "lib"]

pub fn foo() {}


