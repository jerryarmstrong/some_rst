tests/ui/unwind-abis/feature-gate-system-unwind.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the "system-unwind" ABI is feature-gated, and cannot be used when
// the `c_unwind` feature gate is not used.

extern "system-unwind" fn f() {}
//~^ ERROR system-unwind ABI is experimental and subject to change [E0658]

fn main() {
    f();
}


