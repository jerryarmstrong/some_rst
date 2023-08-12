language/move-compiler/src/cfgir/remove_no_ops.rs
=================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use super::{ast::*, cfg::BlockCFG};

/// Returns true if anything changed
pub fn optimize(cfg: &mut BlockCFG) -> bool {
    let mut changed = false;
    for block in cfg.blocks_mut().values_mut() {
        let old_block = std::mem::take(block);
        let old_len = old_block.len();
        *block = old_block
            .into_iter()
            .filter(|c| !c.value.is_unit())
            .collect::<BasicBlock>();
        changed = changed || old_len != block.len();
    }
    changed
}


