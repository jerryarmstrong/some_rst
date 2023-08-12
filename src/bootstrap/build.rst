src/bootstrap/build.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::env;

fn main() {
    let host = env::var("HOST").unwrap();
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rustc-env=BUILD_TRIPLE={}", host);
}


