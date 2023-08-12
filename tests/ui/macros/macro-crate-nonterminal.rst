tests/ui/macros/macro-crate-nonterminal.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:macro_crate_nonterminal.rs

#[macro_use]
extern crate macro_crate_nonterminal;

pub fn main() {
    macro_crate_nonterminal::check_local();
    assert_eq!(increment!(5), 6);
}


