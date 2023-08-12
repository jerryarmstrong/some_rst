tests/ui/feature-gates/feature-gate-prelude_import.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[prelude_import] //~ ERROR `#[prelude_import]` is for use by rustc only
use std::prelude::v1::*;

fn main() {}


