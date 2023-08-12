tests/ui/resolve/pathless-extern-ok.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags:--extern alloc
// build-pass

// Test that `--extern alloc` will load from the sysroot without error.

fn main() {
    let _: Vec<i32> = alloc::vec::Vec::new();
}


