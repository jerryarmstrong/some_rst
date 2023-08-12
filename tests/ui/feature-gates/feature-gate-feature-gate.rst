tests/ui/feature-gates/feature-gate-feature-gate.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![forbid(unstable_features)]
#![feature(intrinsics)] //~ ERROR unstable feature

fn main() { }


