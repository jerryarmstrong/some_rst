tests/ui/cross-crate/moves-based-on-type-cross-crate.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:moves_based_on_type_lib.rs

// pretty-expanded FIXME #23616

extern crate moves_based_on_type_lib;
use moves_based_on_type_lib::f;

pub fn main() {
    f();
}


