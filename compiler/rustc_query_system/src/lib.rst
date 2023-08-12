compiler/rustc_query_system/src/lib.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(assert_matches)]
#![feature(core_intrinsics)]
#![feature(hash_raw_entry)]
#![feature(min_specialization)]
#![feature(extern_types)]
#![allow(rustc::potential_query_instability)]
#![deny(rustc::untranslatable_diagnostic)]
#![deny(rustc::diagnostic_outside_of_impl)]

#[macro_use]
extern crate tracing;
#[macro_use]
extern crate rustc_data_structures;
#[macro_use]
extern crate rustc_macros;

pub mod cache;
pub mod dep_graph;
mod error;
pub mod ich;
pub mod query;
mod values;

pub use error::HandleCycleError;
pub use error::LayoutOfDepth;
pub use error::QueryOverflow;
pub use values::Value;


