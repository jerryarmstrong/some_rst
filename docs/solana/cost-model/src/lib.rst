cost-model/src/lib.rs
=====================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![cfg_attr(RUSTC_WITH_SPECIALIZATION, feature(min_specialization))]
#![allow(clippy::integer_arithmetic)]

pub mod block_cost_limits;
pub mod cost_model;
pub mod cost_tracker;
pub mod transaction_cost;

#[macro_use]
extern crate solana_frozen_abi_macro;


