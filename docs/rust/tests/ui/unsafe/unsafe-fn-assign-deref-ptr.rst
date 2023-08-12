tests/ui/unsafe/unsafe-fn-assign-deref-ptr.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

fn f(p: *mut u8) {
    *p = 0; //~ ERROR dereference of raw pointer is unsafe
    return;
}

fn main() {
}


