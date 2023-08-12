tests/ui/feature-gates/feature-gate-rustc_const_unstable.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test internal const fn feature gate.

#[rustc_const_unstable(feature="fzzzzzt")] //~ stability attributes may not be used outside
pub const fn bazinga() {}

fn main() {
}


