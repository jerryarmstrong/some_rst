tests/ui/inline-const/pat-unsafe-err.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test This is currently broken
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![allow(incomplete_features)]
#![feature(inline_const_pat)]

const unsafe fn require_unsafe() -> usize { 1 }

fn main() {
    match () {
        const {
            require_unsafe();
            //~^ ERROR [E0133]
        } => (),
    }
}


