tests/ui/inline-const/expr-unsafe-err.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck
#![feature(inline_const)]
const unsafe fn require_unsafe() -> usize { 1 }

fn main() {
    const {
        require_unsafe();
        //~^ ERROR [E0133]
    }
}


