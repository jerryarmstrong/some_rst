tests/ui/feature-gates/feature-gate-rustc-attrs-1.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `#[rustc_*]` attributes are gated by `rustc_attrs` feature gate.

#[rustc_variance] //~ ERROR the `#[rustc_variance]` attribute is just used for rustc unit tests and will never be stable
#[rustc_error] //~ ERROR the `#[rustc_error]` attribute is just used for rustc unit tests and will never be stable
#[rustc_nonnull_optimization_guaranteed] //~ ERROR the `#[rustc_nonnull_optimization_guaranteed]` attribute is just used to enable niche optimizations in libcore and libstd and will never be stable

fn main() {}


