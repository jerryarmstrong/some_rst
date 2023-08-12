tests/ui/rustdoc/doc-alias-crate-level.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zdeduplicate-diagnostics=no

#![crate_type = "lib"]

#![doc(alias = "not working!")] //~ ERROR

#[doc(alias = "shouldn't work!")] //~ ERROR
pub struct Foo;


