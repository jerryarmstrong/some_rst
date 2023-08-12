tests/ui/closures/2229_closure_analysis/migrations/old_name.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Ensure that the old name for `rust_2021_incompatible_closure_captures` is still
// accepted by the compiler

#![allow(disjoint_capture_migration)]
//~^ WARN lint `disjoint_capture_migration` has been renamed

fn main() {}


