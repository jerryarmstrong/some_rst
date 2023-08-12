tests/rustdoc/intra-doc/primitive-disambiguators.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]
// @has primitive_disambiguators/index.html
// @has - '//a/@href' '{{channel}}/std/primitive.str.html#method.trim'
//! [str::trim()]


