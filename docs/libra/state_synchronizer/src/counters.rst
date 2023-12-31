state_synchronizer/src/counters.rs
==================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use lazy_static;
use prometheus::{IntCounter, IntGauge};
use solana_libra_metrics::{DurationHistogram, OpMetrics};

lazy_static::lazy_static! {
    pub static ref OP_COUNTERS: OpMetrics = OpMetrics::new_and_registered("state_sync");
}

/// Number of sync requests sent from a node
pub const REQUESTS_SENT: &str = "requests_sent";

/// Number of sync responses a node received
pub const RESPONSES_RECEIVED: &str = "responses_received";

/// Number of Success results of applying a chunk
pub const APPLY_CHUNK_SUCCESS: &str = "apply_chunk_success";

/// Number of failed attempts to apply a chunk
pub const APPLY_CHUNK_FAILURE: &str = "apply_chunk_failure";

lazy_static::lazy_static! {
/// Count the overall number of transactions state synchronizer has retrieved since last restart.
/// Large values mean that a node has been significantly behind and had to replay a lot of txns.
pub static ref STATE_SYNC_TXN_REPLAYED: IntCounter = OP_COUNTERS.counter("state_sync_txns_replayed");

/// Number of peers that are currently active and upstream.
/// They are the set of nodes a node can make sync requests to
pub static ref ACTIVE_UPSTREAM_PEERS: IntGauge = OP_COUNTERS.gauge("active_upstream_peers");

/// Most recent version that has been committed
pub static ref COMMITTED_VERSION: IntGauge = OP_COUNTERS.gauge("committed_version");

/// How long it takes to make progress, from requesting a chunk to processing the response and
/// committing the block
pub static ref SYNC_PROGRESS_DURATION: DurationHistogram = OP_COUNTERS.duration_histogram("sync_progress_duration");

/// Version a node is trying to catch up to
pub static ref TARGET_VERSION: IntGauge = OP_COUNTERS.gauge("target_version");

/// Number of timeouts that occur during sync
pub static ref TIMEOUT: IntCounter = OP_COUNTERS.counter("timeout");
}


