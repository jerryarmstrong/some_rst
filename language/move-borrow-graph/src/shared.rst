language/move-borrow-graph/src/shared.rs
========================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0
use std::collections::{BTreeMap, BTreeSet};

pub fn remap_set<T: Copy + Ord>(set: &mut BTreeSet<T>, id_map: &BTreeMap<T, T>) {
    let _before = set.len();
    *set = std::mem::take(set)
        .into_iter()
        .map(|x| id_map.get(&x).copied().unwrap_or(x))
        .collect();
    let _after = set.len();
    debug_assert!(_before == _after);
}


