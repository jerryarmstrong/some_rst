tests/rustdoc/cfg-doctest.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @!has cfg_doctest/struct.SomeStruct.html
// @!has cfg_doctest/index.html '//a/@href' 'struct.SomeStruct.html'

/// Sneaky, this isn't actually part of docs.
#[cfg(doctest)]
pub struct SomeStruct;


