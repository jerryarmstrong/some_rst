token/cli/tests/config.rs
=========================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    use assert_cmd::cmd::Command;

#[test]
fn invalid_config_will_cause_commands_to_fail() {
    let mut cmd = Command::cargo_bin("spl-token").unwrap();
    let args = &["address", "--config", "~/nonexistent/config.yml"];
    cmd.args(args)
        .assert()
        .stderr("error: Could not find config file `~/nonexistent/config.yml`\n");
    cmd.args(args).assert().code(1).failure();
}


