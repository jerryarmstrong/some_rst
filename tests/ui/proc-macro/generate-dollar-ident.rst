tests/ui/proc-macro/generate-dollar-ident.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Proc macros can generate token sequence `$ IDENT`
// without it being recognized as an unknown macro variable.

// check-pass
// aux-build:generate-dollar-ident.rs

extern crate generate_dollar_ident;
use generate_dollar_ident::*;

macro_rules! black_hole {
    ($($tt:tt)*) => {};
}

black_hole!($var);

dollar_ident!(black_hole);

fn main() {}


