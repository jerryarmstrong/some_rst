devtools/x-core/src/core_config.rs
==================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

/// Core configuration for x.
#[derive(Clone, Serialize, Deserialize, Debug, PartialEq, Eq)]
#[serde(rename_all = "kebab-case")]
pub struct XCoreConfig {
    /// Subsets of this workspace
    pub subsets: BTreeMap<String, SubsetConfig>,
}

#[derive(Clone, Serialize, Deserialize, Debug, PartialEq, Eq)]
#[serde(rename_all = "kebab-case")]
pub struct SubsetConfig {
    /// The root members in this subset
    pub root_members: Vec<String>,
}


