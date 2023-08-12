tests/pretty/attr-tokens-raw-ident.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Keywords in attribute paths are printed as raw idents,
// but keywords in attribute arguments are not.

// pp-exact

#[rustfmt::r#final(final)]
fn main() {}


