tests/testsuite/cargo_add/build_prefer_existing_version/mod.rs
==============================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::compare::assert_ui;
use cargo_test_support::prelude::*;
use cargo_test_support::Project;

use crate::cargo_add::init_alt_registry;

#[cargo_test]
fn build_prefer_existing_version() {
    init_alt_registry();
    let project =
        Project::from_template("tests/testsuite/cargo_add/build_prefer_existing_version/in");
    let project_root = project.root();
    let cwd = &project_root;

    snapbox::cmd::Command::cargo_ui()
        .arg("add")
        .arg_line("cargo-list-test-fixture-dependency --build")
        .current_dir(cwd)
        .assert()
        .success()
        .stdout_matches_path("tests/testsuite/cargo_add/build_prefer_existing_version/stdout.log")
        .stderr_matches_path("tests/testsuite/cargo_add/build_prefer_existing_version/stderr.log");

    assert_ui().subset_matches(
        "tests/testsuite/cargo_add/build_prefer_existing_version/out",
        &project_root,
    );
}


