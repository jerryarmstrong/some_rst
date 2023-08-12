tests/ui/feature-gates/feature-gate-trivial_bounds-lint.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused)]
#![deny(trivial_bounds)] // Ignored without the trivial_bounds feature flag.

struct A where i32: Copy;

fn main() {}


