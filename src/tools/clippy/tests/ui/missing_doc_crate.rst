src/tools/clippy/tests/ui/missing_doc_crate.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::missing_docs_in_private_items)]
#![doc = include_str!("../../README.md")]

fn main() {}


