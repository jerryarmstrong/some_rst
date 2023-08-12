tests/ui/lint/lint-removed-allow.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // No warnings about removed lint when
// allow(renamed_and_removed_lints)

#![allow(renamed_and_removed_lints)]

#[deny(raw_pointer_derive)]
#[deny(unused_variables)]
fn main() { let unused = (); } //~ ERROR unused


