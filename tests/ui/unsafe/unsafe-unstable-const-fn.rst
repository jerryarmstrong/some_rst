tests/ui/unsafe/unsafe-unstable-const-fn.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

#![stable(feature = "foo", since = "1.33.0")]
#![feature(staged_api)]

#[stable(feature = "foo", since = "1.33.0")]
#[rustc_const_unstable(feature = "const_foo", issue = "none")]
const fn unstable(a: *const i32, b: i32) -> bool {
    *a == b
    //~^ dereference of raw pointer is unsafe
}

fn main() {}


