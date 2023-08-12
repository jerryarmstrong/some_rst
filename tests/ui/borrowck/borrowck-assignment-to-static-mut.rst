tests/ui/borrowck/borrowck-assignment-to-static-mut.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Test taken from #45641 (https://github.com/rust-lang/rust/issues/45641)

static mut Y: u32 = 0;

unsafe fn should_ok() {
    Y = 1;
}

fn main() {}


