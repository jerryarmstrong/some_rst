config/generate-keypair/src/main.rs
===================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use solana_libra_generate_keypair::create_faucet_key_file;
use structopt::StructOpt;

#[derive(Debug, StructOpt)]
#[structopt(about = "Tool to generate public/private keypairs")]
struct Args {
    #[structopt(short = "o", long)]
    /// Output file path. Keypair is written to this file
    output: String,
}

fn main() {
    let args = Args::from_args();
    create_faucet_key_file(&args.output);
}


