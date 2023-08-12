tests/ui/lint/lint-renamed-allow.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // No warnings about renamed lint when
// allow(renamed_and_removed_lints)

#![allow(renamed_and_removed_lints)]

#[deny(single_use_lifetime)]
#[deny(unused)]
fn main() { let unused = (); } //~ ERROR unused


