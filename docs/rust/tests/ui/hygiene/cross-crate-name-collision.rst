tests/ui/hygiene/cross-crate-name-collision.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that two items defined in another crate that have identifiers that
// only differ by `SyntaxContext` do not cause name collisions when imported
// in another crate.

// check-pass
// aux-build:needs_hygiene.rs

extern crate needs_hygiene;

use needs_hygiene::*;

fn main() {}


