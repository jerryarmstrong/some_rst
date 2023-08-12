tests/ui/extern-flag/noprelude-and-prelude.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-crate:noprelude:somedep=somedep.rs
// compile-flags: -Zunstable-options --extern somedep
// edition:2018

// Having a flag with `noprelude` and one without, will add to the prelude.

fn main() {
    somedep::somefun();
}


