tests/ui/parser/item-free-const-no-body-syntactic-pass.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Syntactically, a free `const` item can omit its body.

// check-pass

fn main() {}

#[cfg(FALSE)]
const X: u8;


