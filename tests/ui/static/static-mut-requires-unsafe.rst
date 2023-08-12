tests/ui/static/static-mut-requires-unsafe.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

static mut a: isize = 3;

fn main() {
    a += 3;         //~ ERROR: requires unsafe
    a = 4;          //~ ERROR: requires unsafe
    let _b = a;     //~ ERROR: requires unsafe
}


