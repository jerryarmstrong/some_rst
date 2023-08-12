tests/ui/inline-const/pat-unsafe.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test This is currently broken
// check-pass
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![allow(incomplete_features)]
#![warn(unused_unsafe)]
#![feature(inline_const_pat)]

const unsafe fn require_unsafe() -> usize { 1 }

fn main() {
    unsafe {
        match () {
            const {
                require_unsafe();
                unsafe {}
                //~^ WARNING unnecessary `unsafe` block
            } => (),
        }
    }
}


