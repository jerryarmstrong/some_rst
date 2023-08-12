tests/ui/rfcs/rfc-2396-target_feature-11/feature-gate-target_feature_11.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64

#[target_feature(enable = "sse2")] //~ ERROR can only be applied to `unsafe` functions
fn foo() {}

fn main() {}


