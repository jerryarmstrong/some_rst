src/tools/miri/test-cargo-miri/issue-1760/build.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::env;

#[cfg(miri)]
compile_error!("`miri` cfg should not be set in build script");

fn main() {
    // Cargo calls `miri --print=cfg` to populate the `CARGO_CFG_*` env vars.
    // Make sure that the "miri" flag is not set since we are building a procedural macro crate.
    assert!(env::var_os("CARGO_CFG_MIRI").is_none());
}


