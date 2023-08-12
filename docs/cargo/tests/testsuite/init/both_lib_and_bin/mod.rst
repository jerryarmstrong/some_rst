tests/testsuite/init/both_lib_and_bin/mod.rs
============================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::paths;
use cargo_test_support::prelude::*;

use cargo_test_support::curr_dir;

#[cargo_test]
fn both_lib_and_bin() {
    let cwd = paths::root();

    snapbox::cmd::Command::cargo_ui()
        .arg_line("init --lib --bin")
        .current_dir(&cwd)
        .assert()
        .code(101)
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));

    assert!(!cwd.join("Cargo.toml").is_file());
}


