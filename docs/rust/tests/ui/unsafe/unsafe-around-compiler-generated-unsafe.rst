tests/ui/unsafe/unsafe-around-compiler-generated-unsafe.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![deny(unused_unsafe)]

fn main() {
    let _ = async {
        unsafe { async {}.await; } //~ ERROR unnecessary `unsafe`
    };

    // `format_args!` expands with a compiler-generated unsafe block
    unsafe { println!("foo"); } //~ ERROR unnecessary `unsafe`
}


