tests/ui/hygiene/local_inner_macros.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:local_inner_macros.rs

extern crate local_inner_macros;

use local_inner_macros::{public_macro, public_macro_dynamic};

public_macro!();

macro_rules! local_helper {
    () => ( struct Z; )
}

public_macro_dynamic!(local_helper);

fn main() {
    let s = S;
    let z = Z;
}


