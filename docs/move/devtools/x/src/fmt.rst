devtools/x/src/fmt.rs
=====================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::{cargo::Cargo, context::XContext, Result};
use clap::Parser;
use std::ffi::OsString;

#[derive(Debug, Parser)]
pub struct Args {
    #[clap(long)]
    /// Run in 'check' mode. Exits with 0 if input is
    /// formatted correctly. Exits with 1 and prints a diff if
    /// formatting is required.
    check: bool,

    #[clap(long)]
    /// Run check on all packages in the workspace
    workspace: bool,

    #[clap(name = "ARGS", parse(from_os_str), last = true)]
    /// Pass through args to rustfmt
    args: Vec<OsString>,
}

pub fn run(args: Args, xctx: XContext) -> Result<()> {
    // Hardcode that we want imports merged
    let mut pass_through_args = vec!["--config".into(), "imports_granularity=crate".into()];

    if args.check {
        pass_through_args.push("--check".into());
    }

    pass_through_args.extend(args.args);

    let mut cmd = Cargo::new(xctx.config().cargo_config(), "fmt", true);

    if args.workspace {
        // cargo fmt doesn't have a --workspace flag, instead it uses the
        // old --all flag
        cmd.all();
    }

    cmd.pass_through(&pass_through_args).run()
}


