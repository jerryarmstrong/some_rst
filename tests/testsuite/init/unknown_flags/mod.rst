tests/testsuite/init/unknown_flags/mod.rs
=========================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::paths;
use cargo_test_support::prelude::*;

use cargo_test_support::curr_dir;

#[cargo_test]
fn unknown_flags() {
    snapbox::cmd::Command::cargo_ui()
        .arg_line("init foo --flag")
        .current_dir(paths::root())
        .assert()
        .code(1)
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));
}


