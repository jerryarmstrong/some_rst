tests/rustdoc/module-impls.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub use std::marker::Send;

// @!hasraw foo/index.html 'Implementations'


