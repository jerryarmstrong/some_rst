tests/rustdoc/intra-doc/private-failures-ignored.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Rustdoc would previously report resolution failures on items that weren't in the public docs.
// These failures were legitimate, but not truly relevant - the docs in question couldn't be
// checked for accuracy anyway.

#![deny(rustdoc::broken_intra_doc_links)]

/// ooh, i'm a [rebel] just for kicks
struct SomeStruct;


