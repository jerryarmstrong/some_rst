tests/ui/span/multispan-import-lint.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![warn(unused)]

use std::cmp::{Eq, Ord, min, PartialEq, PartialOrd};
//~^ WARN unused imports

fn main() {
    let _ = min(1, 2);
}


