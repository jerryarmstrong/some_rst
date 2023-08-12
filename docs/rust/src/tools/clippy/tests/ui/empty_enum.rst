src/tools/clippy/tests/ui/empty_enum.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![warn(clippy::empty_enum)]
// Enable never type to test empty enum lint
#![feature(never_type)]
enum Empty {}

fn main() {}


