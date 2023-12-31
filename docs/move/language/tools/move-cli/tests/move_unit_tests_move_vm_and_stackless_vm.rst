language/tools/move-cli/tests/move_unit_tests_move_vm_and_stackless_vm.rs
=========================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use move_cli::sandbox::commands::test;

use std::path::{Path, PathBuf};

fn run_all(args_path: &Path) -> datatest_stable::Result<()> {
    let cli_exe = env!("CARGO_BIN_EXE_move");
    let use_temp_dir = !args_path.parent().unwrap().join("NO_TEMPDIR").exists();
    test::run_one(
        args_path,
        &PathBuf::from(cli_exe),
        /* use_temp_dir */ use_temp_dir,
        /* track_cov */ false,
    )?;
    Ok(())
}

// runs all the tests
datatest_stable::harness!(
    run_all,
    "tests/move_unit_tests",
    r"args(\.stackless)?\.txt$"
);


