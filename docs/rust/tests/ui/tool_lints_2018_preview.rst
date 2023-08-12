tests/ui/tool_lints_2018_preview.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(rust_2018_preview)]
#![deny(unknown_lints)]

#[allow(clippy::almost_swapped)]
fn main() {}


