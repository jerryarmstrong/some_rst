tests/testsuite/init/cant_create_library_when_both_binlib_present/mod.rs
========================================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::prelude::*;
use cargo_test_support::Project;

use cargo_test_support::curr_dir;

#[cargo_test]
fn cant_create_library_when_both_binlib_present() {
    let project = Project::from_template(curr_dir!().join("in"));
    let project_root = &project.root();

    snapbox::cmd::Command::cargo_ui()
        .arg_line("init --lib")
        .current_dir(project_root)
        .assert()
        .code(101)
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));
}


