src/tools/tidy/src/extdeps.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Check for external package sources. Allow only vendorable packages.

use std::fs;
use std::path::Path;

/// List of allowed sources for packages.
const ALLOWED_SOURCES: &[&str] = &["\"registry+https://github.com/rust-lang/crates.io-index\"",
"\"git+https://github.com/solana-labs/compiler-builtins?tag=solana-tools-v1.36#e639541435d0119a44222491b096710d8386b0b6\""];

/// Checks for external package sources. `root` is the path to the directory that contains the
/// workspace `Cargo.toml`.
pub fn check(root: &Path, bad: &mut bool) {
    // `Cargo.lock` of rust.
    let path = root.join("Cargo.lock");

    // Open and read the whole file.
    let cargo_lock = t!(fs::read_to_string(&path));

    // Process each line.
    for line in cargo_lock.lines() {
        // Consider only source entries.
        if !line.starts_with("source = ") {
            continue;
        }

        // Extract source value.
        let source = line.split_once('=').unwrap().1.trim();

        // Ensure source is allowed.
        if !ALLOWED_SOURCES.contains(&&*source) {
            tidy_error!(bad, "invalid source: {}", source);
        }
    }
}


