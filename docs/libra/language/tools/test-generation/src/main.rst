language/tools/test-generation/src/main.rs
==========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use solana_libra_test_generation::{config::Args, run_generation};
use structopt::StructOpt;

pub fn main() {
    let args = Args::from_args();
    run_generation(args);
}


