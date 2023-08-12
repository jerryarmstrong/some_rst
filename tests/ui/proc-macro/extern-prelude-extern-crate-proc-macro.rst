tests/ui/proc-macro/extern-prelude-extern-crate-proc-macro.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// edition:2018

extern crate proc_macro;
use proc_macro::TokenStream; // OK

fn main() {}


