src/tools/clippy/tests/ui/crashes/enum-glob-import-crate.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::all)]
#![allow(unused_imports)]

use std::*;

fn main() {}


