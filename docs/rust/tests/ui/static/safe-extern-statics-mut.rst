tests/ui/static/safe-extern-statics-mut.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:extern-statics.rs
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

extern crate extern_statics;
use extern_statics::*;

extern "C" {
    static mut B: u8;
}

fn main() {
    let b = B; //~ ERROR use of mutable static is unsafe
    let rb = &B; //~ ERROR use of mutable static is unsafe
    let xb = XB; //~ ERROR use of mutable static is unsafe
    let xrb = &XB; //~ ERROR use of mutable static is unsafe
}


