language/move-prover/mutation/src/main.rs
=========================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

#![forbid(unsafe_code)]

use itertools::Itertools;
use prover_mutation::mutator;

fn main() {
    let args = std::env::args().collect_vec();
    mutator::mutate(&args[1..]);
}


