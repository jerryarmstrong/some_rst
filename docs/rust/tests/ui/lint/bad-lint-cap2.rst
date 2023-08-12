tests/ui/lint/bad-lint-cap2.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cap-lints deny

#![warn(unused)]
#![deny(warnings)]

use std::option; //~ ERROR

fn main() {}


