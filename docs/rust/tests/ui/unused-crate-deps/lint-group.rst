tests/ui/unused-crate-deps/lint-group.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `unused_crate_dependencies` is not currently in the `unused` group
// due to false positives from Cargo.

// check-pass
// aux-crate:bar=bar.rs

#![deny(unused)]

fn main() {}


