tests/incremental/change_implementation_cross_crate/main.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to reuse `main` despite the changes in the implementation of `foo` and
// `bar`.

// revisions: rpass1 rpass2
// aux-build: a.rs
// compile-flags: -Zquery-dep-graph

#![feature(rustc_attrs)]
#![crate_type = "bin"]
#![rustc_partition_reused(module = "main", cfg = "rpass2")]

extern crate a;

pub fn main() {
    let vec: Vec<u8> = vec![0, 1, 2, 3];
    for b in vec {
        println!("{}", a::foo(b));
        println!("{}", a::bar(b));
    }
}


