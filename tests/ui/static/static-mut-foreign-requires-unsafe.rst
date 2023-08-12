tests/ui/static/static-mut-foreign-requires-unsafe.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

extern "C" {
    static mut a: i32;
}

fn main() {
    a += 3; //~ ERROR: requires unsafe
    a = 4; //~ ERROR: requires unsafe
    let _b = a; //~ ERROR: requires unsafe
}


