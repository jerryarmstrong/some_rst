src/bin/cargo/commands/verify_project.rs
========================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use crate::command_prelude::*;

use std::collections::HashMap;
use std::process;

pub fn cli() -> Command {
    subcommand("verify-project")
        .about("Check correctness of crate manifest")
        .arg_quiet()
        .arg_manifest_path()
        .after_help("Run `cargo help verify-project` for more detailed information.\n")
}

pub fn exec(config: &mut Config, args: &ArgMatches) -> CliResult {
    if let Err(e) = args.workspace(config) {
        config
            .shell()
            .print_json(&HashMap::from([("invalid", e.to_string())]))?;
        process::exit(1)
    }

    config
        .shell()
        .print_json(&HashMap::from([("success", "true")]))?;
    Ok(())
}


