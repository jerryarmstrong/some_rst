tests/rustdoc/intra-doc/prim-assoc.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

//! [i32::MAX]
// @has prim_assoc/index.html '//a[@href="{{channel}}/std/primitive.i32.html#associatedconstant.MAX"]' "i32::MAX"


