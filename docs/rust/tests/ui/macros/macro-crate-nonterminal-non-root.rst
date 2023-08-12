tests/ui/macros/macro-crate-nonterminal-non-root.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:macro_crate_nonterminal.rs

mod foo {
    #[macro_use]
    extern crate macro_crate_nonterminal;  //~ ERROR must be at the crate root
}

fn main() {
}


