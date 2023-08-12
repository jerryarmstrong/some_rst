common/datatest-stable/tests/example.rs
=======================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use solana_libra_datatest_stable::Result;
use std::{fs::File, io::Read, path::Path};

fn test_artifact(path: &Path) -> Result<()> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    Ok(())
}

solana_libra_datatest_stable::harness!(test_artifact, "tests/files", r"^.*/*");


