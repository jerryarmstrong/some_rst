tests/testsuite/init/invalid_dir_name/mod.rs
============================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::paths;
use cargo_test_support::prelude::*;
use std::fs;

use cargo_test_support::curr_dir;

#[cargo_test]
fn invalid_dir_name() {
    let foo = &paths::root().join("foo.bar");
    fs::create_dir_all(foo).unwrap();

    snapbox::cmd::Command::cargo_ui()
        .arg_line("init")
        .current_dir(foo)
        .assert()
        .code(101)
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));

    assert!(!foo.join("Cargo.toml").is_file());
}


