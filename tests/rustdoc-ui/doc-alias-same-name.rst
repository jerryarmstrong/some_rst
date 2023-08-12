tests/rustdoc-ui/doc-alias-same-name.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[doc(alias = "Foo")] //~ ERROR
pub struct Foo;


