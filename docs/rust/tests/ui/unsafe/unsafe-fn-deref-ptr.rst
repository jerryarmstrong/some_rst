tests/ui/unsafe/unsafe-fn-deref-ptr.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

fn f(p: *const u8) -> u8 {
    return *p; //~ ERROR dereference of raw pointer is unsafe
}

fn main() {
}


