tests/ui/lint-unknown-lints-at-crate-level.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -D warnings -D unknown-lints

#![allow(unknown_lints)]
#![allow(random_lint_name)]

fn main() {}


