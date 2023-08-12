compiler/rustc_ast_pretty/src/lib.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustc::untranslatable_diagnostic)]
#![deny(rustc::diagnostic_outside_of_impl)]
#![feature(associated_type_bounds)]
#![feature(box_patterns)]
#![feature(with_negative_coherence)]
#![recursion_limit = "256"]

mod helpers;
pub mod pp;
pub mod pprust;


