language/move-vm/paranoid-tests/tests/tests.rs
==============================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

pub const TEST_DIR: &str = "tests";
use fail::FailScenario;
use move_transactional_test_runner::vm_test_harness::run_test;
use std::path::Path;

fn run_test_(path: &Path) -> Result<(), Box<dyn std::error::Error>> {
    let scenario = FailScenario::setup();
    fail::cfg("verifier-failpoint-1", "100%return").unwrap();
    fail::cfg("verifier-failpoint-2", "100%return").unwrap();
    fail::cfg("verifier-failpoint-3", "100%return").unwrap();
    fail::cfg("verifier-failpoint-4", "100%return").unwrap();
    run_test(path)?;
    scenario.teardown();
    Ok(())
}

datatest_stable::harness!(run_test_, TEST_DIR, r".*\.(mvir|move)$");


