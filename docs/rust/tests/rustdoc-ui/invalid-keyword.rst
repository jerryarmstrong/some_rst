tests/rustdoc-ui/invalid-keyword.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustdoc_internals)]

#[doc(keyword = "foo df")] //~ ERROR
mod foo {}


