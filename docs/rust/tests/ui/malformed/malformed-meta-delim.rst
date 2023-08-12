tests/ui/malformed/malformed-meta-delim.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

#[allow { foo_lint } ]
//~^ ERROR wrong meta list delimiters
//~| HELP the delimiters should be `(` and `)`
fn delim_brace() {}

#[allow [ foo_lint ] ]
//~^ ERROR wrong meta list delimiters
//~| HELP the delimiters should be `(` and `)`
fn delim_bracket() {}


