tests/ui/hygiene/cross-crate-redefine.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that items with identical `SyntaxContext` conflict even when that
// context involves a mark from another crate.

// aux-build:use_by_macro.rs

extern crate use_by_macro;

use use_by_macro::*;

my_struct!(define);
//~^ ERROR the name `MyStruct` is defined multiple times
my_struct!(define);

fn main() {}


