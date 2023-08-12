language/tools/read-write-set/dynamic/src/lib.rs
================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

mod dynamic_analysis;
mod normalize;

pub use dynamic_analysis::{ConcretizedFormals, ConcretizedSecondaryIndexes};
pub use normalize::NormalizedReadWriteSetAnalysis;


