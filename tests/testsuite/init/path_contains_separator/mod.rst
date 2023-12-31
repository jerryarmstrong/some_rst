tests/testsuite/init/path_contains_separator/mod.rs
===================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::compare::assert_ui;
use cargo_test_support::prelude::*;
use cargo_test_support::{t, Project};

use cargo_test_support::curr_dir;

#[cargo_test]
fn path_contains_separator() {
    let project = Project::from_template(curr_dir!().join("in"));
    let project_root = &project.root().join("test:ing");

    if !project_root.exists() {
        t!(std::fs::create_dir(&project_root));
    }

    snapbox::cmd::Command::cargo_ui()
        .arg_line("init --bin --vcs none --edition 2015 --name testing")
        .current_dir(project_root)
        .assert()
        .success()
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));

    assert_ui().subset_matches(curr_dir!().join("out"), project_root);
    assert!(!project_root.join(".gitignore").is_file());
}


