tests/ui/hygiene/cross-crate-name-hiding.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that an item defined by a 2.0 macro in another crate cannot be used in
// another crate.

// aux-build:pub_hygiene.rs

extern crate pub_hygiene;

use pub_hygiene::*;

fn main() {
    let x = MyStruct {};
    //~^ ERROR cannot find struct, variant or union type `MyStruct` in this scope
}


