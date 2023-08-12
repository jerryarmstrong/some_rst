tests/testsuite/cargo_add/git_branch/mod.rs
===========================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use cargo_test_support::compare::assert_ui;
use cargo_test_support::prelude::*;
use cargo_test_support::Project;

use crate::cargo_add::init_registry;
use cargo_test_support::curr_dir;

#[cargo_test]
fn git_branch() {
    init_registry();
    let project = Project::from_template(curr_dir!().join("in"));
    let project_root = project.root();
    let cwd = &project_root;
    let (git_dep, git_repo) = cargo_test_support::git::new_repo("git-package", |project| {
        project
            .file(
                "Cargo.toml",
                &cargo_test_support::basic_manifest("git-package", "0.3.0+git-package"),
            )
            .file("src/lib.rs", "")
    });
    let branch = "dev";
    let find_head = || (git_repo.head().unwrap().peel_to_commit().unwrap());
    git_repo.branch(branch, &find_head(), false).unwrap();
    let git_url = git_dep.url().to_string();

    snapbox::cmd::Command::cargo_ui()
        .arg("add")
        .args(["git-package", "--git", &git_url, "--branch", branch])
        .current_dir(cwd)
        .assert()
        .success()
        .stdout_matches_path(curr_dir!().join("stdout.log"))
        .stderr_matches_path(curr_dir!().join("stderr.log"));

    assert_ui().subset_matches(curr_dir!().join("out"), &project_root);
}


