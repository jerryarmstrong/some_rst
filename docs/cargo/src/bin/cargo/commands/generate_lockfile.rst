src/bin/cargo/commands/generate_lockfile.rs
===========================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use crate::command_prelude::*;

use cargo::ops;

pub fn cli() -> Command {
    subcommand("generate-lockfile")
        .about("Generate the lockfile for a package")
        .arg_quiet()
        .arg_manifest_path()
        .after_help("Run `cargo help generate-lockfile` for more detailed information.\n")
}

pub fn exec(config: &mut Config, args: &ArgMatches) -> CliResult {
    let ws = args.workspace(config)?;
    ops::generate_lockfile(&ws)?;
    Ok(())
}


