language/testing-infra/test-generation/src/main.rs
==================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

#![forbid(unsafe_code)]

use clap::Parser;
use test_generation::{config::Args, run_generation};

fn setup_log() {
    tracing::subscriber::set_global_default(tracing_subscriber::FmtSubscriber::new()).unwrap();
}

pub fn main() {
    setup_log();
    let args = Args::parse();
    run_generation(args);
}


