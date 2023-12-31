storage/libradb/src/schema/mod.rs
=================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This module defines representation of Libra core data structures at physical level via schemas
//! that implement [`solana_libra_schemadb::schema::Schema`].
//!
//! All schemas are `pub(crate)` so not shown in rustdoc, refer to the source code to see details.

pub(crate) mod event;
pub(crate) mod event_accumulator;
pub(crate) mod event_by_key;
pub(crate) mod jellyfish_merkle_node;
pub(crate) mod ledger_counters;
pub(crate) mod ledger_info;
pub(crate) mod signed_transaction;
pub(crate) mod stale_node_index;
pub(crate) mod transaction_accumulator;
pub(crate) mod transaction_by_account;
pub(crate) mod transaction_info;
pub(crate) mod validator;

use failure::prelude::*;
use solana_libra_schemadb::ColumnFamilyName;

pub(super) const EVENT_ACCUMULATOR_CF_NAME: ColumnFamilyName = "event_accumulator";
pub(super) const EVENT_BY_KEY_CF_NAME: ColumnFamilyName = "event_by_key";
pub(super) const EVENT_CF_NAME: ColumnFamilyName = "event";
pub(super) const JELLYFISH_MERKLE_NODE_CF_NAME: ColumnFamilyName = "jellyfish_merkle_node";
pub(super) const LEDGER_COUNTERS_CF_NAME: ColumnFamilyName = "ledger_counters";
pub(super) const STALE_NODE_INDEX_CF_NAME: ColumnFamilyName = "stale_node_index";
pub(super) const SIGNED_TRANSACTION_CF_NAME: ColumnFamilyName = "signed_transaction";
pub(super) const TRANSACTION_ACCUMULATOR_CF_NAME: ColumnFamilyName = "transaction_accumulator";
pub(super) const TRANSACTION_BY_ACCOUNT_CF_NAME: ColumnFamilyName = "transaction_by_account";
pub(super) const TRANSACTION_INFO_CF_NAME: ColumnFamilyName = "transaction_info";
pub(super) const VALIDATOR_CF_NAME: ColumnFamilyName = "validator";

fn ensure_slice_len_eq(data: &[u8], len: usize) -> Result<()> {
    ensure!(
        data.len() == len,
        "Unexpected data len {}, expected {}.",
        data.len(),
        len,
    );
    Ok(())
}


