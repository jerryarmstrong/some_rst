tests/ui-fulldeps/internal-lints/existing_doc_keyword.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z unstable-options

#![feature(rustc_private)]
#![feature(rustdoc_internals)]

#![crate_type = "lib"]

#![deny(rustc::existing_doc_keyword)]

#[doc(keyword = "tadam")] //~ ERROR
mod tadam {}


