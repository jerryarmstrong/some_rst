tests/ui/unsafe/issue-45087-unreachable-unsafe.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verify that unreachable code undergoes unsafety checks.
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

fn main() {
    return;
    *(1 as *mut u32) = 42;
    //~^ ERROR dereference of raw pointer is unsafe
}

fn panic() -> ! {
    panic!();
}

fn f(a: *mut u32) {
    panic();
    *a = 1;
    //~^ ERROR dereference of raw pointer is unsafe
}

enum Void {}

fn uninhabited() -> Void {
    panic!();
}

fn g(b: *mut u32) {
    uninhabited();
    *b = 1;
    //~^ ERROR dereference of raw pointer is unsafe
}


