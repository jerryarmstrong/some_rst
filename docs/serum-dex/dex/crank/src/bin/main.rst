dex/crank/src/bin/main.rs
=========================

Last edited: 2021-05-20 03:21:28

Contents:

.. code-block:: rs

    use anyhow::Result;
use clap::Clap;
use crank::Opts;

fn main() -> Result<()> {
    let opts = Opts::parse();
    crank::start(None, opts)
}


