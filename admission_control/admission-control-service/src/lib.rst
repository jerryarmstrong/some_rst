admission_control/admission-control-service/src/lib.rs
======================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

#![deny(missing_docs)]

//! Admission Control
//!
//! Admission Control (AC) is the public API end point taking public gRPC requests from clients.
//! AC serves two types of request from clients:
//! 1. SubmitTransaction, to submit transaction to associated validator.
//! 2. UpdateToLatestLedger, to query storage, e.g. account state, transaction log, and proofs.

/// AC gRPC service.
pub mod admission_control_service;
#[cfg(any(test, feature = "fuzzing"))]
/// Useful Mocks
pub mod mocks;
use lazy_static::lazy_static;
use solana_libra_metrics::OpMetrics;

lazy_static! {
    static ref OP_COUNTERS: OpMetrics = OpMetrics::new_and_registered("admission_control");
}


