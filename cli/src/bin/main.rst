cli/src/bin/main.rs
===================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_cli::Opts;
use anyhow::Result;
use clap::Parser;

fn main() -> Result<()> {
    anchor_cli::entry(Opts::parse())
}


