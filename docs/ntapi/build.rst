build.rs
========

Last edited: 2023-04-20 23:00:37

Contents:

.. code-block:: rs

    use std::env::var;

fn main() {
    #[cfg(feature = "user")] {
        if var("TARGET").map(
            |t| t == "x86_64-pc-windows-gnu" || t == "i686-pc-windows-gnu"
        ).unwrap_or(false) {
            if var("WINAPI_NO_BUNDLED_LIBRARIES").is_ok() {
                println!("cargo:rustc-link-lib=ntdll");
            } else {
                println!("cargo:rustc-link-lib=winapi_ntdll");
            }
        }
    }
}


