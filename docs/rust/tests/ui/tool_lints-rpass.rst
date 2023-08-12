tests/ui/tool_lints-rpass.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(unknown_lints)]

#[allow(clippy::almost_swapped)]
fn main() {}


