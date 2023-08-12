tests/ui/lint/bad-lint-cap3.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --cap-lints warn

#![warn(unused)]
#![deny(warnings)]

use std::option; //~ WARN

fn main() {}


