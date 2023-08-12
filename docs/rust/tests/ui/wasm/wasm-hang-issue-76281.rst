tests/ui/wasm/wasm-hang-issue-76281.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-wasm32
// compile-flags: -C opt-level=2
// build-pass

// Regression test for #76281.
// This seems like an issue related to LLVM rather than
// libs-impl so place here.

fn main() {
    let mut v: Vec<&()> = Vec::new();
    v.sort_by_key(|&r| r as *const ());
}


