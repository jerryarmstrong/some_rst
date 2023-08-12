install/build.rs
================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use std::time::SystemTime;

fn main() {
    println!(
        "cargo:rustc-env=TARGET={}",
        std::env::var("TARGET").unwrap()
    );
    println!(
        "cargo:rustc-env=BUILD_SECONDS_SINCE_UNIX_EPOCH={}",
        SystemTime::now()
            .duration_since(SystemTime::UNIX_EPOCH)
            .unwrap()
            .as_secs(),
    );
}


