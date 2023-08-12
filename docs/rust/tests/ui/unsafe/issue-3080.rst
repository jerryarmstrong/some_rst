tests/ui/unsafe/issue-3080.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

struct X(());
impl X {
    pub unsafe fn with(&self) { }
}

fn main() {
    X(()).with(); //~ ERROR requires unsafe function or block
}


