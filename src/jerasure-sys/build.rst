src/jerasure-sys/build.rs
=========================

Last edited: 2021-11-23 13:45:37

Contents:

.. code-block:: rs

    extern crate cc;

fn main() {
    cc::Build::new()
        .files(&[
            "jerasure/src/galois.c",
            "jerasure/src/jerasure.c",
            "jerasure/src/reed_sol.c",
            "jerasure/src/cauchy.c",
            "jerasure/src/liberation.c",
        ])
        .include("jerasure/include")
        .include("gf-complete/include")
        .compile("Jerasure");
    println!("cargo:rustc-link-lib=static=Jerasure");
}


