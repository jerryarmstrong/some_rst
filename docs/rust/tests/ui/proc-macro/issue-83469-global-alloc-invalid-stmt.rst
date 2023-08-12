tests/ui/proc-macro/issue-83469-global-alloc-invalid-stmt.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #83469
// Ensures that we recover from `#[global_alloc]` on an invalid
// stmt without an ICE

fn outer() {
    #[global_allocator]
    fn inner() {} //~ ERROR allocators must be statics
}

fn main() {}


