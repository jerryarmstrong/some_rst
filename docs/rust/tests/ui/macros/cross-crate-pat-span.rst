tests/ui/macros/cross-crate-pat-span.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// check-pass
// aux-build: foreign-crate-macro-pat.rs
//
// Tests that the edition of the foreign crate is used
// when determining the behavior of the `:pat` matcher.

extern crate foreign_crate_macro_pat;

fn main() {
    let _b = foreign_crate_macro_pat::custom_matches!(b'3', b'0' ..= b'9');
}


