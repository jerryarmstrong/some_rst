tests/ui/use/use-paths-as-items.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Each path node in a `use` declaration must be treated as an item. If not, the following code
// will trigger an ICE.
//
// Related issue: #25763

use std::{mem, ptr};
use std::mem; //~ ERROR the name `mem` is defined multiple times

fn main() {}


