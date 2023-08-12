tests/ui/extern-flag/noprelude.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-crate:noprelude:somedep=somedep.rs
// compile-flags: -Zunstable-options
// edition:2018

fn main() {
    somedep::somefun();  //~ ERROR failed to resolve
}


