tests/ui/resolve/macro-determinacy-non-module.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

use std as line;

const C: u32 = line!();

fn main() {}


