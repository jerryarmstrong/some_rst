tests/testsuite/init/ignores_failure_to_format_source/mod.rs
============================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::compare::assert_ui;
use cargo_test_support::prelude::*;
use cargo_test_support::Project;

use cargo_test_support::curr_dir;

#[cargo_test]
fn ignores_failure_to_format_source() {
    let project = Project::from_template(curr_dir!().join("in"));
    let project_root = &project.root();

    snapbox::cmd::Command::cargo_ui()
        .arg_line("init --lib --vcs none")
        .env("PATH", "") // pretend that `rustfmt` is missing
        .current_dir(project_root)
        .assert()
        .success()
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));

    assert_ui().subset_matches(curr_dir!().join("out"), project_root);
}


