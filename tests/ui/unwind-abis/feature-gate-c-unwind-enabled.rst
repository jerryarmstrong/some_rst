tests/ui/unwind-abis/feature-gate-c-unwind-enabled.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the "C-unwind" ABI is feature-gated, and *can* be used when the
// `c_unwind` feature gate is enabled.

// check-pass

#![feature(c_unwind)]

extern "C-unwind" fn f() {}

fn main() {
    f();
}


