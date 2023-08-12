tests/incremental/auxiliary/issue-49482-reexport.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
extern crate issue_49482_macro_def;

pub use issue_49482_macro_def::*;

pub fn foo() {}


