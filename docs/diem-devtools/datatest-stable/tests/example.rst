datatest-stable/tests/example.rs
================================

Last edited: 2022-02-01 05:13:53

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// SPDX-License-Identifier: MIT OR Apache-2.0

use datatest_stable::Result;
use std::{fs::File, io::Read, path::Path};

fn test_artifact(path: &Path) -> Result<()> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    Ok(())
}

datatest_stable::harness!(test_artifact, "tests/files", r"^.*/*");


