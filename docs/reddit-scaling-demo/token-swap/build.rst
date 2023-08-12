token-swap/build.rs
===================

Last edited: 2020-08-26 08:56:56

Contents:

.. code-block:: rs

    extern crate cbindgen;

use std::env;

fn main() {
    let crate_dir = env::var("CARGO_MANIFEST_DIR").unwrap();
    cbindgen::generate(&crate_dir)
        .unwrap()
        .write_to_file("inc/token-swap.h");
}


