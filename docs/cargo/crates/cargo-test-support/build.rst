crates/cargo-test-support/build.rs
==================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    fn main() {
    println!(
        "cargo:rustc-env=NATIVE_ARCH={}",
        std::env::var("TARGET").unwrap()
    );
    println!("cargo:rerun-if-changed=build.rs");
}


