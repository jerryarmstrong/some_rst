tests/rustdoc/intra-doc/extern-crate.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:intra-link-extern-crate.rs

// When loading `extern crate` statements, we would pull in their docs at the same time, even
// though they would never actually get displayed. This tripped intra-doc-link resolution failures,
// for items that aren't under our control, and not actually getting documented!

#![deny(rustdoc::broken_intra_doc_links)]

extern crate inner;


