tests/ui/lint/lint-non-snake-case-crate-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-name NonSnakeCase
// error-pattern: crate `NonSnakeCase` should have a snake case name

#![deny(non_snake_case)]

fn main() {}


