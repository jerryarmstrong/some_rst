tests/ui/generator/issue-45729-unsafe-in-generator.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![feature(generators)]

fn main() {
    let _ = || {
        *(1 as *mut u32) = 42;
        //~^ ERROR dereference of raw pointer is unsafe
        yield;
    };
}


