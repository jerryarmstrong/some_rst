tests/ui/unsafe/unsafe-fn-called-from-safe.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

unsafe fn f() { return; }

fn main() {
    f();
    //[mir]~^ ERROR call to unsafe function is unsafe
    //[thir]~^^ ERROR call to unsafe function `f` is unsafe
}


