program-runtime/src/lib.rs
==========================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![cfg_attr(RUSTC_WITH_SPECIALIZATION, feature(min_specialization))]
#![deny(clippy::integer_arithmetic)]
#![deny(clippy::indexing_slicing)]
#![recursion_limit = "2048"]

#[macro_use]
extern crate eager;

#[macro_use]
extern crate solana_metrics;

pub use solana_rbpf;
pub mod accounts_data_meter;
pub mod compute_budget;
pub mod invoke_context;
pub mod loaded_programs;
pub mod log_collector;
pub mod message_processor;
pub mod pre_account;
pub mod prioritization_fee;
pub mod stable_log;
pub mod sysvar_cache;
pub mod timings;


