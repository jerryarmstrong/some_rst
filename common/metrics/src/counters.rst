common/metrics/src/counters.rs
==============================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

#[cfg(feature = "service-metrics")]
use crate::ServiceMetrics;
use lazy_static::lazy_static;
use prometheus::IntCounter;

#[cfg(feature = "service-metrics")]
lazy_static! {
    pub static ref SVC_COUNTERS: ServiceMetrics = ServiceMetrics::new_and_registered();
}

lazy_static! {
    // Admission Control counters
    pub static ref COUNTER_ADMISSION_CONTROL_CANNOT_SEND_REPLY: IntCounter = register_int_counter!(
        "COUNTER_ADMISSION_CONTROL_CANNOT_SEND_REPLY",
        "Number of errors related to send reply in Admission Control"
    ).unwrap();

    // Client counters
    pub static ref COUNTER_CLIENT_ERRORS: IntCounter = register_int_counter!(
        "COUNTER_CLIENT_ERRORS",
        "Number of errors encountered by Client"
    ).unwrap();
}


