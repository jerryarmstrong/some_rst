tests/ui/proc-macro/invalid-punct-ident-4.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:invalid-punct-ident.rs
// needs-unwind proc macro panics to report errors

#[macro_use]
extern crate invalid_punct_ident;

lexer_failure!();
//~^ ERROR proc macro panicked
//~| ERROR unexpected closing delimiter: `)`

fn main() {
    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


