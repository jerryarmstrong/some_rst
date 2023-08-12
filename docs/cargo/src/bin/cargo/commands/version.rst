src/bin/cargo/commands/version.rs
=================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use crate::cli;
use crate::command_prelude::*;

pub fn cli() -> Command {
    subcommand("version")
        .about("Show version information")
        .arg_quiet()
        .after_help("Run `cargo help version` for more detailed information.\n")
}

pub fn exec(config: &mut Config, args: &ArgMatches) -> CliResult {
    let verbose = args.verbose() > 0;
    let version = cli::get_version_string(verbose);
    cargo::drop_print!(config, "{}", version);
    Ok(())
}


