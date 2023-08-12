tests/ui/proc-macro/invalid-punct-ident-3.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:invalid-punct-ident.rs
// needs-unwind proc macro panics to report errors

#[macro_use]
extern crate invalid_punct_ident;

invalid_raw_ident!(); //~ ERROR proc macro panicked

fn main() {}


