tests/ui-fulldeps/create-dir-all-bare.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::env;
use std::fs;
use std::path::PathBuf;

fn main() {
    let path = PathBuf::from(env::var_os("RUST_TEST_TMPDIR").unwrap());
    env::set_current_dir(&path).unwrap();
    fs::create_dir_all("create-dir-all-bare").unwrap();
}


