tests/testsuite/init/no_filename/mod.rs
=======================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::paths;
use cargo_test_support::prelude::*;

use cargo_test_support::curr_dir;

#[cfg(not(windows))]
#[cargo_test]
fn no_filename() {
    snapbox::cmd::Command::cargo_ui()
        .arg_line("init /")
        .current_dir(paths::root())
        .assert()
        .code(101)
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));
}


