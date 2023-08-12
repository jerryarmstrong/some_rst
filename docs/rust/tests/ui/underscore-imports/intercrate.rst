tests/ui/underscore-imports/intercrate.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:underscore-imports.rs

extern crate underscore_imports;

use underscore_imports::*;

fn main() {
    ().in_scope1();
    ().in_scope2();
}


