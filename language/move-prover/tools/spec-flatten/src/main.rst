language/move-prover/tools/spec-flatten/src/main.rs
===================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use anyhow::Result;
use clap::Parser;

use spec_flatten::{run, FlattenOptions};

fn main() -> Result<()> {
    let options = FlattenOptions::parse();
    run(&options)
}


