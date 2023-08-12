consensus/src/chained_bft/consensusdb/schema/mod.rs
===================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

pub(crate) mod block;
pub(crate) mod quorum_certificate;
pub(crate) mod single_entry;

use failure::prelude::*;
use solana_libra_schemadb::ColumnFamilyName;

pub(super) const BLOCK_CF_NAME: ColumnFamilyName = "block";
pub(super) const QC_CF_NAME: ColumnFamilyName = "quorum_certificate";
pub(super) const SINGLE_ENTRY_CF_NAME: ColumnFamilyName = "single_entry";

fn ensure_slice_len_eq(data: &[u8], len: usize) -> Result<()> {
    ensure!(
        data.len() == len,
        "Unexpected data len {}, expected {}.",
        data.len(),
        len,
    );
    Ok(())
}


