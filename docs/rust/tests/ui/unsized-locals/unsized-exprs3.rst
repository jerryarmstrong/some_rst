tests/ui/unsized-locals/unsized-exprs3.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:ufuncs.rs

extern crate ufuncs;

use ufuncs::udrop;

fn main() {
    udrop as fn([u8]);
    //~^ERROR E0277
}


