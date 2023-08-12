tests/ui/extern/extern-crate-rename.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:m1.rs
// aux-build:m2.rs


extern crate m1;
extern crate m2 as m1; //~ ERROR is defined multiple times

fn main() {}


