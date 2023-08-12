tests/ui/extern-flag/noprelude-resolves.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-crate:noprelude:somedep=somedep.rs
// compile-flags: -Zunstable-options
// edition:2018

// `extern crate` can be used to add to prelude.
extern crate somedep;

fn main() {
    somedep::somefun();
}


