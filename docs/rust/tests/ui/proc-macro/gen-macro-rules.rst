tests/ui/proc-macro/gen-macro-rules.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Derive macros can generate `macro_rules` items, regression test for issue #63651.

// check-pass
// aux-build:gen-macro-rules.rs

extern crate gen_macro_rules as repro;

#[derive(repro::repro)]
pub struct S;

m!(); // OK

fn main() {}


